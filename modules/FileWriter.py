#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet
import os

from modules.Enums import TextEngines
from modules.Functions import print_info, print_error


class FileWriter():
    def __init__(self):
        self.__text_engines = {
            TextEngines.docx.value: self.__save_to_docx,
            TextEngines.txt.value: self.__save_to_txt}

    def save_to_file(self, filename: str, file_extension: str, text: str, ):
        try:
            self.__text_engines[file_extension.lower()](filename, text)
        except KeyError:
            print_error(f"Расширение {file_extension} не поддерживается!")
            raise EOFError

    def __save_to_docx(self, filename: str, text: str):
        pass

    def __save_to_txt(self, filename: str, text: str):
        name = os.path.join(os.getcwd(), f"{filename}_UniSize.txt")
        file = open(name, encoding="UTF-8", mode="a")
        file.writelines(text)
        file.close()
        print_info(f"Текст сохранён в файл: {name}")
