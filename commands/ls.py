import os
from utils.print_utils import print
from utils.get_file_colors import get_file_color
from colorama import Fore
import colorama
from typing import Optional

colorama.init(autoreset=True)


def execute(core, directory: Optional[str] = None):
    # Borrowed from old core
    files = os.listdir(directory)
    files.sort()
    if directory is None:
        directory = os.getcwd()
    print(f"╭ {Fore.CYAN}{directory}")
    for item in files:
        color = get_file_color(item, os.getcwd())
        print(Fore.RESET + color + "| " + item)
    if files == []:
        print(f"{Fore.LIGHTMAGENTA_EX} nothing to see here :p")
