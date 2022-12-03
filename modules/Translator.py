#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from __future__ import annotations

import translators as tss

from modules.Enums import LanguageCodes
from modules.Enums import SchemeTransformation
from modules.Functions import print_info


class Translator:

    def __init__(self, text: str, language: LanguageCodes | str,
                 scheme_transformation: SchemeTransformation, translator: str,
                 iterations: int):
        self.__text = text
        self.__translator = translator
        self.__buffer = text
        self.__language = language
        self.__buffer_lang = language
        self.__schema = scheme_transformation.split(",")
        self.__iterations = iterations

    def __trace_schema(self, text, lang):
        self.__buffer = tss.translate_text(query_text=text, translator=self.__translator,
                                           from_language=self.__buffer_lang, to_language=lang)
        # print(self.buffer)
        self.__buffer_lang = lang

    def __trace_iterations(self):
        for j in self.__schema:
            print_info(f"Сейчас перевожу на {j}.")
            self.__trace_schema(text=self.__buffer, lang=j)
        print_info(f"Сейчас перевожу на {self.__language}")
        self.__text = tss.translate_text(query_text=self.__buffer, translator=self.__translator,
                                         from_language=self.__buffer_lang, to_language=self.__language)

    def text_translation(self):
        # print(f"Начальный текст: {self.text}")

        for i in range(self.__iterations):
            self.__trace_iterations()

    def get_text(self) -> str:
        return self.__text
