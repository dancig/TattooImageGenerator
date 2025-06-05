import torch
from diffusers import DiffusionPipeline

# Модуль генерации изображений
class ImageGenerator:
    isBusy = False  # Значение занятости модуля. True - занят генерацией, False - ожидает генерации

    # Функция инициализации пайплайна модели
    # Принимает путь до модели, тип данных для вычислений, вариант модели, использование safetensors, safety_checker
    # Инициализирует пайнлайн модели с указанными настройками
    def __init__(self, path_to_model, torch_type, variant, safetensors, safety_checker):
        self.sd_pipeline = DiffusionPipeline.from_pretrained(path_to_model,
                                                             torch_dtype=torch_type,
                                                             variant=variant,
                                                             use_safetensors=safetensors,
                                                             safety_checker=safety_checker).to("cuda")
    # Функция загрузки LoRA весов
    # Принимает путь к папке с весами и название файла весов
    # Загружает веса в пайплайн
    def load_lora(self, path_to_lora_folder, weight_name):
        self.sd_pipeline.load_lora_weights(path_to_lora_folder, weight_name=weight_name)

    # Функция генерации изображения
    # Принимает строку текстового запроса и количество шагов шумоподавления
    # Запускает генерацию изображения
    # Возвращает сгенерированное изображение
    def generate_image(self, prompt, steps):
        return self.sd_pipeline(prompt, num_inference_steps=steps).images[0]
