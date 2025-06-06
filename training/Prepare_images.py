from PIL import Image
import os

images = []

for image_file in os.listdir('./input_images/'):
    images.append(image_file)

# Проход по каждому изображению
for i in range(len(images)):
    image = Image.open(f'./input_images/{images[i]}')

    # Если на изображение в формате PNG, то заменяем прозрачные пиксели на белые и удаляем канал прозрачности
    if image.mode == 'RGBA':
        image.load()
        new_image = Image.new('RGB', image.size, (255, 255, 255))
        new_image.paste(image, mask=image.split()[3])
        image = new_image
    image = image.convert('RGB')

    # Изменяем разрешение изображений, сохраняя соотношение сторон
    if image.width > image.height:
        new_width = 512
        new_height = int(image.height * (new_width / image.width))
    else:
        new_height = 512
        new_width = int(image.width * (new_height / image.height))
    image_resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Сохраняем изображения с названиями 1.png, 2.png и т.д.
    image_resized.save(f'./output_images/{i+1}.png', format='PNG', compress_level=0)
