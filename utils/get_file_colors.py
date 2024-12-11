import os
from colorama import Fore
import colorama

colorama.init(autoreset=True)


def get_file_color(filename, dir):
    _, ext = os.path.splitext(filename.lower())
    if ext == '.py':
        return Fore.CYAN
    elif ext == '.exe' or os.access(f"{dir}/{ext}", os.X_OK):
        return Fore.YELLOW
    elif ext == '.zip' or ext == ".tar.gz":
        return Fore.RED
    else:
        return Fore.RESET
