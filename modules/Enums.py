#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet

from enum import Enum

DEFAULT_COUNT_CHARS = 1500


class TextEngines(Enum):
    docx = ".docx"
    txt = ".txt"


class SchemeTransformation(Enum):
    # ru -> en -> nl -> en -> ru
    Scheme_1_to_reverso = "en,nl,en"
    Scheme_2_to_reverso = "en,nl,tr,en"


class Translators(Enum):
    google = "google"
    yandex = "yandex"
    deepl = "deepl"
    reverso = "reverso"


class LanguageCodes(Enum):
    RU = "ru"
    EN = "en"
