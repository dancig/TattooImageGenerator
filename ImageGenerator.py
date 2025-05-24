import torch
from diffusers import DiffusionPipeline

# Модуль генерации изображений
class ImageGenerator:
    isBusy = False  # Значение занятости модуля. True - занят генерацией, False - ожидает генерации

    # Функция инициализации пайплайна модели StableDiffusion1.5
    def __init__(self):
        self.sd_pipeline = DiffusionPipeline.from_pretrained("./stable-diffusion-v1-5", torch_dtype=torch.bfloat16,
                                                             use_safetensors=True, safety_checker=None).to("cuda")

    # Функция генерации изображения
    # Принимает строку текстового запроса
    # Запускает генерацию изображения с количеством шагов шумоподавления = 30
    # Возвращает сгенерированное изображение
    def generate_image(self, prompt):
        return self.sd_pipeline(prompt, num_inference_steps=30).images[0]
