from googletrans import Translator
import asyncio

# Модуль перевода текста
class TranslatorModule:

    # Функция перевода текста на английский язык
    # Принимает строку текстового запроса
    # Возвращает переведенную на английский язык строку, если она написана не на английском языке,
    # Иначе возвращает строку без изменений
    async def translate(self, text):
        async with Translator() as translator:
            if (await translator.detect(text)).lang == 'en':
                return text
            else:
                return (await translator.translate(text=text, src='ru', dest='en')).text

    # Функция запуска перевода
    # Принимает строку текстового запроса
    # Запускает перевод и возвращает строку переведенную на английский язык
    def translate_text(self, text):
        return asyncio.run(self.translate(text))