from flask import Flask, request, render_template
from ImageGenerator import ImageGenerator
from Translator import TranslatorModule
import os
import time
import traceback

app = Flask(__name__)
images_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = images_folder
imageGen = ImageGenerator()
translator = TranslatorModule()


# Функция обработки запросов
# Возвращает страницу "base.html", если запрос "GET"
# Если метод запроса не "POST", то возвращается шаблон "base.html"
# Если текстовой строки нет в запросе или длина строки превышает 500 символов или длина меньше или равна нулю, то
# возвращается шаблон "base.html" с аргументами last_prompt = "" и isBadPrompt=True
# Если модуль генерации изображений занят, то возвращается шаблон "base.html" с аргументами last_prompt=текстовый запрос
# и isBusy = True
# Если метод запроса "POST", текст запроса прошел валидацию и модуль генерации изображений не занят, то запускается
# перевод текстового запроса на английский, запускается генерация изображения по переведенному тексту,
# изображение сохраняется с именем файла - дата и время завершения генерации, возвращается шаблон "base.html"
# с аргументами last_prompt = текстовый запрос, image = путь до сгенерированного изображения
# Если происходят ошибки, то возвращается шаблон "base.html" с аргументами last_prompt = "" и error = True,
# текст ошибки выводится в консоль
@app.route("/", methods=['GET', 'POST'])
def process_requests():
    try:
        if request.method != 'POST':
            return render_template('base.html')     # Если метод не "POST"
        if ("prompt" not in request.form) or (len(request.form["prompt"]) > 500) or (len(request.form["prompt"]) <= 0):
            return render_template('base.html', last_prompt="", isBadPrompt=True)   # Если текстовый запрос
                                                                                    # не прошел валидацию
        if imageGen.isBusy == True:
            return render_template('base.html', last_prompt=request.form["prompt"], isBusy=True)    # Если модуль
                                                                                        # генерации изображений занят
        try:
            imageGen.isBusy = True
            prompt = request.form["prompt"]
            translated_prompt = translator.translate_text(prompt)  # Перевод текстового запроса на английский
            print(translated_prompt)
            image = imageGen.generate_image(translated_prompt)  # Генерация изображения по текстовому запросу
            filename = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(time.time()))    # Название файла -
                                                                                        # текущая дата и время
            image.save(f"static/images/{filename}.png")  # Сохранение сгенерированного изображения
            saved_image = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}.png")
            imageGen.isBusy = False
            return render_template('base.html', last_prompt=prompt, image=saved_image)
        except Exception:   # Ошибка произошла на этапе обработки запроса
            traceback.print_exc()
            imageGen.isBusy = False
            return render_template('base.html', last_prompt="", error=True)
    except Exception:   # Ошибка произошла на этапе проверки запроса
        traceback.print_exc()
        return render_template('base.html', last_prompt="", error=True)


if __name__ == "__main__":
    app.run(debug=False)
