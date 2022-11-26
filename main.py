#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from __future__ import annotations

from modules.Enums import LanguageCodes, SchemeTransformation, Translators
from modules.Translator import Translator


class UniSizer:
    def __init__(self, text: str, language: LanguageCodes | str, iterations: int = 1,
                 translator: Translator | str = Translators.reverso.value,
                 scheme_transformation: SchemeTransformation | str = SchemeTransformation.Scheme_1_to_reverso.value):
        self.text = text
        self.language = language
        self.iterations = iterations
        self.translator = translator
        self.scheme_transformation = scheme_transformation

    def uniqueization(self):
        tr = Translator(text=self.text, language=self.language, iterations=self.iterations, translator=self.translator,
                        scheme_transformation=self.scheme_transformation)
        tr.text_translation()


if __name__ == "__main__":
    uni = UniSizer(text=input("Введите текст: "), language="en", scheme_transformation="ru,nl,ru")
    uni.uniqueization()
