import json
import pathlib

path = pathlib.Path('./output_images')

# Читаем пути к файлам в списки
captions = list(path.glob('*.txt'))
images = list(path.glob('*.png'))

# Создаем словарь из ключа: название файла без расширения и значения: путь к файлу
images = {image.stem: image for image in images}

# Cоздаем словарь из ключа: путь к txt файлу и значения: путь к одноименному png файлу
caption_image = {caption: images.get(caption.stem) for caption in captions if images.get(caption.stem)}

# Создаем файл metadata.jsonl и записываем туда словарь ключ:file_name и значение: название файла изображения,
# ключ: prompt и значение текст описания файла изображения
metadata = path.joinpath('metadata.jsonl')
with metadata.open('w', encoding='utf-8') as file:
    for caption, image in caption_image.items():
        text = caption.read_text(encoding='utf-8')
        json.dump({'file_name': image.name, 'prompt': text}, file)
        file.write("\n")
