# TattoImageGenerator
Веб-приложение для генерации татуировок по текстовому запросу

## Структура репозитория
```
├── models
│   └── pytorch_lora_weights.safetensors        Веса дообученой модели
│
├── static
│   ├── images                                  Папка для хранения изображений
│   │   └── (...).png                           Примеры генерируемых изображений
│   │
│   ├── download.js                             Скрипт сохранения изображений
│   ├── image_no_bg.png                         Замещающее изображение
│   ├── remove_background_request.js            Скрипт отправки запроса на удаление фона
│   ├── styles.css                              Файл со стилями CSS
│   └── validate.js                             Скрипт валидации текстового запроса
│
├── templates
│   └── base.html                               Шаблон веб-страницы
│
├── tests
│   ├── download.test.js                        Юнит-тесты функции сохранения изображений
│   ├── test_server.py                          Юнит-тесты функции обработки запросов
│   └── validate.test.js                        Юнит-тесты функции валидации текста
│
├── training
│   ├── dataset                                 Набор данных для обучения
│   │   ├── 1.png
│   │   ├── 1.txt
│   │   ├── ...
│   │   ├── 50.png
│   │   ├── 50.txt
│   │   └── metadata.jsonl
│   │
│   ├── Create_dataset.py                       Скрипт для создания файла описания набора данных
│   ├── DreamBoothLoRATraining.ipynb            Скрипт обучения модели
│   └── Prepare_images.py                       Скрипт обработки изображений набора данных
│
├── ImageGenerator.py                           Модуль генерации изображений
├── ImageProcessor.py                           Модуль обработки изображений
├── Server.py                                   Серверный модуль
└── Translator.py                               Модуль перевода текста
```