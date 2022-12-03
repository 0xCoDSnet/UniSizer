#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from modules.Enums import DEFAULT_COUNT_CHARS
from modules.FileReader import FileReader
from modules.Functions import print_info


class WordSeparator:
    # Текст в 2 тысячи знаков это ~ 230-270 слов
    def __init__(self, text):
        self.__text = text
        self.__text_words = self.__text.split()
        # self.__text_words = re.findall(r'\w+', self.__text)
        self.__count_words = len(self.__text_words)
        self.__count_chars = len(self.__text)

    def get_count_chars(self):
        return self.__count_chars

    def separator(self) -> list[str]:
        def separ(self, words_i):
            chars = 0
            text = ""
            while (chars <= DEFAULT_COUNT_CHARS):
                try:
                    current_word = " " + self.__text_words[words_i]
                except IndexError:
                    break
                if (chars + len(current_word)) <= DEFAULT_COUNT_CHARS:
                    text += current_word
                    chars += len(current_word)
                    words_i += 1
                else:
                    break
            return text, len(text.split())

        print_info(f"Chars: {self.__count_chars}")
        print_info(f"Words: {self.__count_words}")

        current_count_words = 0
        list_text = []

        while (current_count_words < self.__count_words):
            text, words = separ(self, current_count_words)
            current_count_words += words
            list_text.append(text)
        return list_text


if __name__ == '__main__':
    my_file = "test.txt"
    fr = FileReader(my_file).get_text()
    text_l = WordSeparator(fr).separator()
    print(text_l)
