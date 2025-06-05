from flask import Flask, request, render_template
from ImageGenerator import ImageGenerator
from Translator import TranslatorModule
from ImageProcessor import ImageProcessor
import torch
import argparse
import os
import time
import traceback

app = Flask(__name__)
images_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = images_folder

# Функция парсинга аргументов
# Возвращает объект с аргументами
def parse_arguments():
    parser = argparse.ArgumentParser()

    # Путь к директории с моделью генерации изображений
    parser.add_argument('--model_path',
                        required=True,
                        type=str,
                        help='Path to diffusion model folder')

    # Количество шагов генерации изображения
    parser.add_argument('--steps',
                        default=30,
                        type=int,
                        help='Number of inference steps (default=30)')

    # Тип данных для вычислений генератора
    parser.add_argument('--torchtype',
                        default=torch.bfloat16,
                        help='Type of torch data (default=torch.bfloat16)')

    # Вариант весов модели генерации изображений
    parser.add_argument('--variant',
                        default='fp16',
                        type=str,
                        help='Variant of weight file (default="fp16")')

    # Использование весов .safetensors
    parser.add_argument('--safetensors',
                        default=True,
                        type=bool,
                        help='Load from safetensors weights (default=True)')

    # Название модуля проверки изображения на безопасность
    parser.add_argument('--safetychecker',
                        default=None,
                        help='Name of safetychecker (default=None)')

    # Ключевое слово, которое будет добавляться в промпт
    parser.add_argument('--keyword',
                        default='Tattoosketch',
                        type=str,
                        help='Keyword for generation prompt (default="Tattoosketch")')

    # Использование LoRA весов
    parser.add_argument('--lora',
                        default=True,
                        type=bool,
                        help='Enable LoRA (default=True)')

    # Путь к директории с весами LoRA
    parser.add_argument('--lora_path',
                        default='./models',
                        type=str,
                        help='Path to LoRA folder (default="./models")')

    # Название файла весов LoRA
    parser.add_argument('--lora_filename',
                        default='TattooSketch-10.safetensors',
                        type=str,
                        help='LoRA filename (default="TattooSketch-10.safetensors")')

    # Пороговое значение для удаления фона со сгенерированного изображения
    parser.add_argument('--threshold',
                        default=40,
                        type=int,
                        help='White background removing threshold [0-255] (default=40)')

    # Использование модуля перевода текста
    parser.add_argument('--translator',
                        default=True,
                        type=bool,
                        help='Enable translator module (default=True)')
    return parser.parse_args()

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
        # Если метод не "POST"
        if request.method != 'POST':
            return render_template('base.html')

        # Если текстовый запрос не прошел валидацию
        if ("prompt" not in request.form) or (len(request.form["prompt"]) > 500) or (len(request.form["prompt"]) <= 0):
            return render_template('base.html',
                                   last_prompt="",
                                   isBadPrompt=True)

        # Если модуль генерации изображений занят
        if imageGen.isBusy == True:
            return render_template('base.html',
                                   last_prompt=request.form["prompt"],
                                   isBusy=True)

        try:
            imageGen.isBusy = True
            prompt = request.form["prompt"]
            # Если модуль перевода включен
            if enable_translator:
                # Перевод текстового запроса на английский
                translated_prompt = translator.translate_text(prompt)
                prompt = translated_prompt

            # Добавить к промту ключевое слово
            prompt = keyword + " " + prompt
            print(prompt)

            # Генерация изображения по текстовому запросу
            image = imageGen.generate_image(prompt, steps)
            imageGen.isBusy = False

            # Название файла - текущая дата и время
            filename = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(time.time()))

            # Сохранение сгенерированного изображения
            image.save(f"static/images/{filename}.png")
            saved_image = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}.png")

            imageProcessor.remove_background(images_folder, filename)
            saved_image_no_bg = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}_no_bg.png")
            return render_template('base.html',
                                   last_prompt=request.form["prompt"],
                                   image=saved_image,
                                   image_no_bg=saved_image_no_bg)
        # Ошибка произошла на этапе обработки запроса
        except Exception:
            traceback.print_exc()
            imageGen.isBusy = False
            return render_template('base.html',
                                   last_prompt="",
                                   error=True)
    # Ошибка произошла на этапе проверки запроса
    except Exception:
        traceback.print_exc()
        return render_template('base.html',
                               last_prompt="",
                               error=True)


if __name__ == "__main__":
    args = parse_arguments()
    steps = args.steps
    keyword = args.keyword
    enable_translator = args.translator
    imageGen = ImageGenerator(args.model_path, args.torchtype, args.variant, args.safetensors, args.safetychecker)

    # Если модуль LoRA включен
    if args.lora == True:
        imageGen.load_lora(args.lora_path, args.lora_filename)
        print(f"LoRA weight loaded from {args.lora_path}/{args.lora_filename}")

    translator = TranslatorModule()
    imageProcessor = ImageProcessor()

    app.run(debug=False)
