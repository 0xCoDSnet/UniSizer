#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet
import os

from modules.Enums import TextEngines


class FileWriter():
    def __init__(self):
        self.__text_engines = {
            TextEngines.docx.value: self.__save_to_docx,
            TextEngines.txt.value: self.__save_to_txt}

    def save_to_file(self, filename: str, file_extension: str, text: str, ):
        try:
            self.__text_engines[file_extension.lower()](filename, text)
        except KeyError:
            raise EOFError(f"Расширение {file_extension} не поддерживается!")

    def __save_to_docx(self, filename: str, text: str):
        pass

    def __save_to_txt(self, filename: str, text: str):
        name = os.path.join(os.getcwd(), f"{filename}_UniSize.txt")
        file = open(name, encoding="UTF-8", mode="w")
        file.writelines(text)
        file.close()
        print(f"Текст сохранён в файл: {name}")
