from flask import Flask, request, render_template
from ImageGenerator import ImageGenerator
from Translator import TranslatorModule
import os
import time

app = Flask(__name__)
images_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = images_folder
imageGen = ImageGenerator()
translator = TranslatorModule()


# Функция обработки запросов
# Возвращает страницу "base.html", если запрос "GET"
# Если запрос "POST", текст запроса существует, его длина больше 0 и меньше или равна 500
# и модуль генерации изображений не занят генерацией, то текстовый запрос переводится на английский,
# генерируется и сохраняется изображение, возвращается страница "base.html" с аргументами:
# last_prompt = последний текстовый запрос, image =  путь к сгенерированному изображению
# Если запрос "POST", текстовый запрос прошел валидацию и модуль генерации изображений занят генерацией,
# то возвращается страница "base.html" с аргументами: last_prompt = последний текстовый запрос и isBusy = True
# Если запрос "POST" и текстовый запрос не прошел валидацию, то возвращается страница "base.html" с аргументами:
# last_prompt = пустая строка, isBadPrompt = True
@app.route("/", methods=['GET', 'POST'])
def process_requests():
    if request.method == 'POST':
        if ("prompt" in request.form) and (len(request.form["prompt"]) <= 500) and (len(request.form["prompt"]) > 0):
            if imageGen.isBusy == False:  # Запрос "POST" и модуль генерации не занят
                imageGen.isBusy = True
                prompt = request.form["prompt"]
                translated_prompt = translator.translate_text(prompt)  # Перевод текстового запроса на английский
                print(translated_prompt)
                image = imageGen.generate_image(translated_prompt)  # Генерация изображения по текстовому запросу
                filename = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(time.time()))  # Название файла -
                                                                                          # текущая дата и время
                image.save(f"static/images/{filename}.png")  # Сохранение сгенерированного изображения
                saved_image = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}.png")
                imageGen.isBusy = False
                return render_template('base.html', last_prompt=prompt, image=saved_image)
            else:
                return render_template('base.html', last_prompt=request.form["prompt"], isBusy=True)
        else:
            return render_template('base.html', last_prompt="", isBadPrompt=True)
    else:
        return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=False)
