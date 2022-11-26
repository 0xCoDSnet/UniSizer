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

        self.division_line = "-" * 13

    @staticmethod
    def trace_schema(self, text, lang):
        self.buffer = tss.translate_text(query_text=text, translator=self.translator,
                                         from_language=self.buffer_lang, to_language=lang)
        print(self.buffer)
        self.buffer_lang = lang

    @staticmethod
    def trace_iterations(self):
        for j in self.schema:
            print(f"Сейчас перевожу на {j}")
            self.trace_schema(self, text=self.buffer, lang=j)
        print(f"Сейчас перевожу на {self.language}")
        self.text = tss.translate_text(query_text=self.buffer, translator=self.translator,
                                       from_language=self.buffer_lang, to_language=self.language)

    def text_translation(self):
        print(f"Главный язык: {self.language} | Схема перевода: {self.schema} | Итераций: {self.iterations}")
        print(f"Начальный текст: {self.text}")
        print(self.division_line)

        for i in range(self.iterations):
            self.trace_iterations(self)

        print(self.division_line)
        print("Итог:")
        print(self.text)
