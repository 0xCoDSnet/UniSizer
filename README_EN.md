Readme Lang: [EN](https://github.com/0xCoDSnet/UniSizer/blob/main/README_EN.md)/[RU](https://github.com/0xCoDSnet/UniSizer/blob/main/README.md)

**UniSizer** - Text Uniquizer, a software (script) that helps make a test unique! It is based on the translation from one language to another. Thanks to this you can achieve the uniqueness of the text, and most importantly not to lose its meaning!

## To-Do
- [x] Translating Readme.md to EN (through an interpreter)
- [ ] Adding web interface
- [ ] Search Schemes, for different languages
- [x] Add text limit bypass
- [ ] Support for files
  - [x] **txt** _read/write_
  - [x] **docx** _read/write txt_
  - [ ] pdf
- [x] Flexible customization via CLI
- [x] Different platform applications:
  - [x] **Win** _(Tested on Win 10, 64-bit)_ 
  - [ ] Linux
  - [ ] Android 
  - [ ] iOS

## Contents
- [Why is UniSizer better than Synonymizers?](#why-is-unisizer-better-than-synonymizers)
- [UniSizer vs Synonymizers comparison](#comparison-of-unisizer-with-synonymizers)
  - [Text Conversion Comparison with Synonymizers](#comparison-of-text-conversion-with-synonymizers)
  - [Text uniqueness and comprehensibility comparison with Synonymizers](#comparison-of-text-uniqueness-and-comprehensibility-with-synonymizers)
  - [Systems (sites) for checking text uniqueness](#systems-sites-to-check-the-uniqueness-of-the-text)
- [Setup guide](#installation-instructions)
- [Command Line Arguments](#command-line-arguments)
- [Example program execution](#example-program-execution)
- [Example use-code](#example-usage-from-the-code)
  - [Change language](#change-language-default-ru)
  - [Change the number of iterations](#change-the-number-of-iterations-default-1)
  - [Change interpreter](#change-the-translator-default-reverso)
  - [Change translation scheme/translation path](#change-translation-schemepath-default-scheme_1_to_reversoennlen)
- [License](#license)
## Why is UniSizer better than synonymizers?

First, the big problem with synonymizers is that they replace words with synonyms, and sometimes synonyms can be very strange, and if the text is still large, it will be difficult to correct by hand.

Secondly, synonymizers do not change the structure of the text, do not change introductory words, participles, participles and other aspects of language.

**UniSizer** solves these problems and makes the text unlike the original one for anti-plagiarism analyzers. Also, thanks to iterations of text processing you can adjust the degree of text distortion.

---

## Comparison of UniSizer with Synonymizers

### Comparison of text conversion with Synonymizers:
Text | UniSizer | Synonymizer by RusTXT | Synonymizer by Textovod
------------ | ------------ | ------------ | ------------
The relationship between the terms "short story" and "novella" has not received an unambiguous interpretation in Russian, and formerly Soviet, literary scholarship. Most languages do not know the difference between these terms at all. B. V. Tomashevsky calls the short story a specifically Russian synonym for the international term "novella"[11]. B.M. Eichenbaum, another representative of the formalist school, suggested that these concepts should be distinguished on the grounds that the short story is narrative, and the narration is more psychological and reflective, and closer to the narrativeless essay. Goethe already pointed to the sharpness of the short story when he considered the subject of the short story to be "the occurrence of an unheard event"[12]. In this interpretation, the short story and the essay are two opposite hypostases of the story.|The relationship between the terms "short story and short story" has not been clearly interpreted in Russian and earlier Soviet literary studies. Most languages do not know the difference. B. V. Tomashevsky specifically refers to the story with the international term "novel."[11] Another representative of the formalist school, B. M. Eikenbaum, proposed to dilute these concepts on the basis that the novel is a plot and the story is psychological and reflective, closer to an unreliable sketch. The novel's poignancy was emphasized by Goethe, who viewed it as the subject of an "unprecedented event." [12]. In this interpretation, the novel and the essay are two opposite hypostases of the story.| The correspondence between the terms "short story" and "novella" has not earned a single interpretation in Russian, and above all Russian, literary scholarship. Most syllables are unaware of the discrepancy between these considerations. Tomashevsky dubs the short story an unconventional Russian synonym for the international term "novella."[11] Another agent of the formalist school, B. Eichenbaum, suggested diluting these definitions on the grounds that the short story is plot-driven, while the short story is more psychological and reflective, closer to the plotless essay. Goethe already pointed to the sharpness of the novel as an object of the "accomplished, unparalleled event"[12]. Under this explanation, the story and the essay are two opposite hypostases of the story.|The relationship between the concepts "story" and "novella" has not received an obvious treatment in American, and formerly Soviet, literary scholarship. Most languages do not know the difference between these concepts at all. B. V. Yakobson calls retelling a specifically Ukrainian synonym for the interstate term "novella"[11]. Another representative of the gymnasium of formalism, B. M. Tynian, proposed to divorce these concepts on the grounds that the novella is plot-driven and the retelling is more realistic and reflexive, further to the storyless collection. The poignancy of the short story was pointed out by Goethe, who regarded its subject as "the accomplished unprecedented event."[12] In this interpretation, the novella and the essay are two opposing essences of the story.
The precursors of mathematical analysis were the ancient method of exhaustion and the method of indivisibles. All three directions, including analysis, have a common initial idea: decomposition into infinitesimal elements, the nature of which, however, seemed rather vague to the authors of the idea. Algebraic approach (calculus of infinitesimals) begins to appear in Wallis, James Gregory and Barrow. Newton created the new calculus as a system in its entirety, but he did not publish his discoveries for a long time[2]. | The forerunners of calculus were the old method of exhaustion and the indivisible method.   All three directions, including analysis, had a common basic idea: Decomposition in infinitely many elements, the nature of which, however, seemed rather uncertain.   The algebraic approach (infinitesimal calculus) begins to appear in Wallis, James Gregory, and Barrow.   Newton created a new system of calculus, but did not publish his discoveries for a long time[2]. | The forerunners of exact parsing were the classical recipe for exhaustion and the recipe for the indivisible. All three approaches, starting with analysis, were united by a common initial idea: destruction for unboundedly insignificant elements, the nature of which, however, was rather vague as far as the makers of the idea were concerned. The algebraic approach (calculus of unboundedly small elements) initiated by Wallis, James Gregory and Barrow. In the full frontier, the newfangled calculus as an arrangement was created by Newton, who, however, did not publish his discoveries for a long time.2].| The forerunners of physical and mathematical analysis were the ancient Greek method of exhaustion and the method of the indivisible. All four directions, including express-analysis, share a common initial concept: decomposition into infinitesimal components, the nature of which, however, seemed rather vague to the reviewers of the idea. A mathematical approach (counting infinitesimally small ones) is beginning to emerge from Wallis, James Henry, and Barrow. In the fullest measure the newest calculus as a systematic system was created by Isaac Newton, who, however, did not publish his discoveries for a long time[2].

*Settings* ***UniSizer:*** **Text Conversion:** Main Language: ru , Translation Scheme: "en, nl, en", Iterations: 1*

### Comparison of text uniqueness and comprehensibility with Synonymizers:

*The text uniqueness rating (in %): 0 - 40 - ❌ ; 41 - 60 - ⚠ ; 61 - 100 - ✔*
Text / Verification System (Uniqueness in %) | RusTXT | Anitiplagiat.ru (Free) | Textovod | Text sense / comprehensibility 
------------ | ------------ | ------------ | ------------ | -------- 
Copied 1 text | 0% - ❌ | 0% - ❌ | 0% - ❌ | Original 
Copied 2 text | 0% - ❌ | 0% - ❌ | 0% - ❌ | Original 
UniSizer (1 text) | 98.5% - ✔ | 100% - ✔ | 85% - ✔ | ✔ - The meaning is almost indistinguishable from the original, there are inaccuracies in the word conversion. But if you tweak it a little, you can get a good text. 
UniSizer (2 text) | 87.5% - ✔ | 100% - ✔ | 49% - ⚠| ✔ - The meaning is not lost, the text is completely understandable. 
Synonymizer from RusTXT (1 text) |82.6% - ✔ | 69.99% - ✔ | 58% - ⚠| ⚠ - The text has a logical component, but the meaning is almost no. The text is full of epithets and Old Russian words, which distorts the comprehensibility of the text. 
Synonymizer by RusTXT (2 text) | 94.5% - ✔ | 100% - ✔ | 66 % - ✔| ❌ - There is no sense in the text, it is not clear what we are talking about. 
Synonymizer by Tekstovod (1 text) | 100% - ✔ | 100% - ✔ | 95% - ✔ | ⚠ - The logic is there, but the main idea is distorted, from this the clarity and meaning of the text suffered. 
Synonymizer from Tekstovod (2 text) | 100% - ✔ | 100% - ✔ | 57% - ⚠ | ⚠ - The thought in the text is traced, but it is filled with unnecessary epithets and words, making it difficult to perceive the text.

**If you set the scheme correctly and choose the number of iterations, you can get a high level of uniqueness of the text.**

### Systems (sites) to check the uniqueness of the text:
- [RusTXT-Antiplagiat](https://rustxt.ru/antiplagiat)
- [TextCompare - Comparing Texts before/after Transformations](https://textcompare.ru/)
- [Antiplagiat.ru](https://www.antiplagiat.ru/)
- [TextCompare - Synonymizer/Antiplagiat](https://textovod.com/synonymizer)

---

## Installation instructions 
1. Make sure you have Python **version 3.9 or higher installed.**
2. Install the dependencies by running the command `python3 -m pip install -r requirements.txt`.
3. To run the program, execute the command `python3 UniSizer.py`.
## Command line arguments
```
usage: UniSizer.py [-h] --input INPUT [-output OUTPUT] --language LANG [--translator TRANSLATOR] [--iterations ITER] [--schema SCHEMA]

--Unicator text, a software (script) which helps to make a test unique! It is based on the translation from one language to another. Thanks to this you can achieve the uniqueness of the text, and most importantly not to lose its meaning!

optional arguments:
  -h, --help            show this help message and exit
  --input               INPUT Type text or path to file.
  --output              OUTPUT Enter name of output file
  --language            LANG Enter text language.
  --translator TRANSLATOR
                        Enter name of translator. Default: reverso ; All: reverso,google,yandex,deepl
  --Enter the number of repetitions ITER. Default: 1
  --schema SCHEMA Enter your scheme/translation path. Default: en,nl,en
```
## Example program execution
```
$ python3 UniSizer.py --input=test.txt --language=en
[INFO] Text will be written to the file!
---------------------------------------------------------
Main language: ru | translation scheme: en,nl,en | iterations: 1
---------------------------------------------------------
[INFO] Now translating to en.
[INFO] Now translating to nl.
[INFO] Now translating to en.
[INFO] Now translating to ru.
[INFO] Text saved to file: E:\My Desktop\Learning\Programming\Projects\UniSizer\test_UniSize.txt
```
## Example usage from the code
### Change language (Default: Ru):
String input or pass through a variable:
```py
lang = "en" # ru,uk,nl,kk and others 
uni = UniSizer(text=input(), language=lang)
```
or with LanguageCodes(Enum):
```py
from Enums import LanguageCodes
uni = UniSizer(text=input(), language=LanguageCodes.EN.value) 
```
### Change the number of iterations (Default: 1):
Integer input:
```py
uni = UniSizer(text=input(), language="ru", iterations=3) # iterations:int!
```
### Change the translator (Default: Reverso):
Line Input:
```py
uni = UniSizer(text=input(), language="ru", translator="google")
```
or with Translators(Enum):
```py
from Enums import Translators
uni = UniSizer(text=input(), language="ru", translator=Translators.google.value)
```
### Change translation scheme/path (Default: Scheme_1_to_reverso="en,nl,en"):
String input:
```py
uni = UniSizer(text=input(), language="ru", scheme_transformation="en,uk,nl,en")
```
or with SchemeTransformation(Enum):
```py
from Enums import SchemeTransformation
uni = UniSizer(text=input(), language="ru", scheme_transformation=SchemeTransformation.Scheme_2_to_reverso.value)
```

---

## License
[MIT Llicense](https://github.com/0xCoDSnet/UniSizer/blob/main/LICENSE)
