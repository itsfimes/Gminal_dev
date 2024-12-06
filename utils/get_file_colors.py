import os
from colorama import Fore
import colorama

colorama.init(autoreset=True)


def get_file_color(filename):
    _, ext = os.path.splitext(filename.lower())
    if ext == '.py':
        return Fore.CYAN
    elif ext == '.exe':
        return Fore.YELLOW
    elif ext == '.zip':
        return Fore.RED
    else:
        return Fore.RESET
