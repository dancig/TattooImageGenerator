from googletrans import Translator
import asyncio


class TranslatorModule:

    async def translate(self, text):
        async with Translator() as translator:
            return (await translator.translate(text=text, src='ru', dest='en')).text

    def translate_text(self, text):
        return asyncio.run(self.translate(text))

