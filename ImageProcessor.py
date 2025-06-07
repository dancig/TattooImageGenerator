from PIL import Image
import numpy as np

# Обработчик изображений
class ImageProcessor:

    # Функция эрозии изображения
    # Принимает массив пикселей
    # Проходит по массиву пикселей, если пиксель непрозрачный и вокруг него есть прозрачные пиксели,
    # то делает пиксель прозрачным
    def erosion(self, pixels):
        new_pixels = pixels.copy()
        for i in range(1, len(pixels[0]) - 1):
            for j in range(1, len(pixels) - 1):
                # Если пиксель непрозрачный
                if pixels[i, j, 3] == 255:
                    # Если среди соседних пикселей есть прозрачный
                    if (pixels[i - 1:i + 2, j - 1:j + 2, 3] == 0).any():
                        # Сделать пиксель прозрачным
                        new_pixels[i, j, 3] = 0
        return new_pixels

    # Функция дилатации изображения
    # Принимает массив пикселей
    # Проходит по массиву пикселей, если пиксель непрозрачный, то делает пиксели вокруг него непрозрачными и черными
    # Возвращает массив новых пикселей
    def dilation(self, pixels):
        new_pixels = pixels.copy()
        for i in range(1, len(pixels[0]) - 1):
            for j in range(1, len(pixels) - 1):
                # Если пиксель непрозрачный
                if pixels[i, j, 3] == 255:
                    # Сделать пиксели вокруг и сам пиксель непрозрачными и черного цвета
                    new_pixels[i - 1:i + 2, j - 1:j + 2, 3] = 255
                    new_pixels[i - 1:i + 2, j - 1:j + 2, :3] = 0
        return new_pixels

    # Функция удаления цвета выше порогового значения на изображении
    # Принимает путь к директории с файлом, имя файла, пороговое значение,
    # булевые значения выполнения операций эрозии и дилатации
    # Конвертирует изображение в формат RGBA и делает прозрачными пиксели, цвет которых выше порогового значения
    # Применяет функции эрозии и дилатации, если аргументы == True
    # Сохраняет изображение в формате PNG, в той же директории, добавляя к названию "_no_bg"
    def remove_background(self, path, filename, threshold=40, erode=False, dilate=False):
        image = Image.open(f'{path}/{filename}.png')
        image = image.convert('RGBA')
        pixels = np.asarray(image).copy()
        # Если все компоненты цвета пикселя больше порога, то сделать пиксель прозрачным
        pixels[:, :, 3] = (255 * (pixels[:, :, :3] < threshold).all(axis=2)).astype(np.uint8)
        if erode == True:
            pixels = self.erosion(pixels)
        if dilate == True:
            pixels = self.dilation(pixels)
        new_image = Image.fromarray(pixels)
        new_image.save(f'{path}/{filename}_no_bg.png', format='PNG')
