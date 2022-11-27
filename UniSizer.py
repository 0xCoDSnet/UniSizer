#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from __future__ import annotations

import argparse
from pathlib import Path

from modules.Enums import LanguageCodes, SchemeTransformation, Translators
from modules.FileReader import FileReader
from modules.FileWriter import FileWriter
from modules.Translator import Translator


def get_args():
    parser = argparse.ArgumentParser(description="--test--")

    parser.add_argument("--input", help="Введите текст или путь к файлу.", dest="input", type=str, required=True)
    parser.add_argument("--output", help="Введите название выходного файла", dest="output", type=str)
    parser.add_argument("--language", help="Введите язык текста.", dest="lang", type=str, required=True)

    parser.add_argument("--translator",
                        help="Введите название переводчика. Default: reverso ; All: reverso,google,yandex,deepl ",
                        dest="translator", default="reverso", type=str)
    parser.add_argument("--iterations", help="Введите количество повторений. Default: 1", dest="iter", default=1,
                        type=int)
    parser.add_argument("--schema", help="Введите свою схему/путь перевода. Default: en,nl,en", dest="schema",
                        default="en,nl,en", type=str)

    args = parser.parse_args()

    my_file = Path(args.input)

    if my_file.is_file():  # get text from file; Or return text
        print("Текст будет выведен в файл!")
        fr = FileReader(my_file)
        if args.output is None:
            filename, file_extension = fr.get_file_type(args.input)
        else:
            filename, file_extension = fr.get_file_type(args.output)
        args.input = fr.get_text()  # get text from file

        return args.input, args.lang, args.translator, args.iter, args.schema, filename, file_extension
    else:
        print("Текст будет выведен в консоль!")
    return args.input, args.lang, args.translator, args.iter, args.schema, None, None


class UniSizer:
    def __init__(self, text: str,
                 language: LanguageCodes | str,
                 filename: str = None,
                 file_extension: str = None,
                 iterations: int = 1,
                 translator: Translator | str = Translators.reverso.value,
                 scheme_transformation: SchemeTransformation | str = SchemeTransformation.Scheme_1_to_reverso.value):
        self.__text = text
        self.__language = language
        self.__iterations = iterations
        self.__translator = translator
        self.__scheme_transformation = scheme_transformation
        self.__filename = filename
        self.__file_extension = file_extension

    def uniqueization(self):
        tr = Translator(text=self.__text, language=self.__language, iterations=self.__iterations,
                        translator=self.__translator,
                        scheme_transformation=self.__scheme_transformation)
        tr.text_translation()
        text = tr.get_text()

        if (self.__filename is not None) and (self.__file_extension is not None):
            fw = FileWriter()
            fw.save_to_file(filename=self.__filename, file_extension=self.__file_extension, text=text)

        else:
            print(text)


if __name__ == "__main__":
    input_text, lang, translator, iterations, schema, filename, file_extension = get_args()
    uni = UniSizer(filename=filename, file_extension=file_extension, text=input_text, language=lang,
                   iterations=iterations,
                   translator=translator,
                   scheme_transformation=schema)
    uni.uniqueization()
