from enum import Enum


class SchemeTransformation(Enum):
    # ru -> en -> nl -> en -> ru
    Scheme_reverso = "en,nl,en"


class Translators(Enum):
    google = "google"
    yandex = "yandex"
    deepl = "deepl"
    reverso = "reverso"


class LanguageCodes(Enum):
    RU = "ru"
    EN = "en"
