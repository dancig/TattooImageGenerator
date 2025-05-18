from googletrans import Translator
import asyncio

# Модуль перевода текста
class TranslatorModule:

    # Функция перевода текста на английский язык
    # Принимает строку текстового запроса
    # Возвращает переведенную на английский язык строку
    async def translate(self, text):
        async with Translator() as translator:
            return (await translator.translate(text=text, src='ru', dest='en')).text
    # Функция запуска перевода
    # Принимает строку текстового запроса
    # Запускает перевод и возвращает строку переведенную на английский язык
    def translate_text(self, text):
        return asyncio.run(self.translate(text))

