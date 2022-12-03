#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

import os

import docx

from modules.Enums import TextEngines
from modules.Functions import print_error


class FileReader():

    def __init__(self, path_to_file):
        self.__text_engines = {
            TextEngines.docx.value: self.__get_text_docx,
            TextEngines.txt.value: self.__get_text_txt}

        self.__text_in_file = None
        self.__filename, self.__file_extension = self.get_file_type(path_to_file)
        self.__get_text_from_file(path_to_file, self.__file_extension)

    def __composing_text(self, text_list: list) -> str:
        text = ""
        for line in text_list:
            text += line
        return text

    def __get_text_txt(self, path_to_file: str) -> str:
        return self.__composing_text(open(path_to_file, encoding="UTF-8", mode="r").readlines())

    def __get_text_docx(self, path_to_file: str) -> str:
        doc = docx.Document(path_to_file)
        all_paras = [f"{line.text}\n" for line in doc.paragraphs if line.text]
        return self.__composing_text(all_paras)

    def __get_text_from_file(self, path_to_file: str, file_extension: str):
        try:
            self.__text_in_file = self.__text_engines[file_extension.lower()](path_to_file)
        except KeyError:
            print_error(f"Расширение {file_extension} не поддерживается!")
            raise EOFError

    def get_text(self):
        return self.__text_in_file

    @staticmethod
    def get_file_type(path_to_file):
        return os.path.splitext(path_to_file)


if __name__ == "__main__":
    path_to_file = input("Path to file: ")
    f = FileReader(path_to_file)
    print(f.get_text())
