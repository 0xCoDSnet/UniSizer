#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from __future__ import annotations

import translators as tss

from modules.Enums import LanguageCodes
from modules.Enums import SchemeTransformation


class Translator:
    def __init__(self, text: str, language: LanguageCodes | str,
                 scheme_transformation: SchemeTransformation, translator: str,
                 iterations: int):
        self.text = text
        self.translator = translator
        self.buffer = text
        self.language = language
        self.buffer_lang = language
        self.schema = scheme_transformation.split(",")
        self.iterations = iterations

    def text_translation(self):
        print(f"Главный язык: {self.language} | Схема перевода: {self.schema} | Итераций: {self.iterations}")
        print(f"Начальный текст: {self.text}")
        print("-" * 10)

        def trace_schema(text, lang):
            self.buffer = tss.translate_text(query_text=text, translator=self.translator,
                                             from_language=self.buffer_lang, to_language=lang)
            print(self.buffer)
            self.buffer_lang = lang
            # print(f"Получилось:{self.buffer}")

        def trace_iterations():
            for j in self.schema:
                print(f"Сейчас перевожу на {j}")
                trace_schema(text=self.buffer, lang=j)
            print(f"Сейчас перевожу на {self.language}")
            self.text = tss.translate_text(query_text=self.buffer, translator=self.translator,
                                           from_language=self.buffer_lang, to_language=self.language)

        for i in range(self.iterations):
            trace_iterations()

        print("-" * 10)
        print("Итог:")
        print(self.text)
