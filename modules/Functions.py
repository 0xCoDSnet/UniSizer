#  Author: 0xCoDSnet
#  GitHub: https://github.com/0xCoDSnet
#  GitLab: https://gitlab.com/0xCoDSnet
from colorama import init, Fore


def start_colorama():
    init()


def print_in_lines(text):
    line = "-" * len(text)
    print(line)
    print(Fore.WHITE + text + Fore.RESET)
    print(line)


def print_info(text):
    print(Fore.LIGHTYELLOW_EX + f"[INFO] {text}" + Fore.RESET)


def print_warning(text):
    print(Fore.LIGHTRED_EX + f"[WARNING] {text}" + Fore.RESET)


def print_error(text):
    print(Fore.RED + f"[ERROR] {text}" + Fore.RESET)


if __name__ == "__main__":
    print_in_lines("123")
    print_info("123")
    print_warning("123")
    print_error("123")
