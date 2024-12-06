# Override the built-in print function with our custom one, yes I know this is cursed
import builtins
import sys
import colorama
from colorama import Fore, Back, Style  # Theoretically used
import os
from tqdm import tqdm



colorama.init(autoreset=True)


def print(message="", style=None):
    """Customizable print function for Gminal."""
    if style == 'bold':
        builtins.print(f"\033[1m{message}\033[0m")  # ANSI escape code for bold text
    elif style == 'underline':
        builtins.print(f"\033[4m{message}\033[0m")  # ANSI escape code for underline
    else:
        builtins.print(f"{message}")  # Default style


def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


def tqdm_bar(*args, **kwargs):
    return tqdm(*args, **kwargs)


def write_progress(task_name, progress):
    # Creates a progress bar with a width of 10 characters
    bar_width = 10
    filled_length = int(bar_width * progress // 100)
    bar = '■' * filled_length + '/' * (bar_width - filled_length)

    # Format each line with task name, progress bar, and percentage
    sys.stdout.write(f"\r{task_name:<15} |{bar}| {progress:3}%")
    sys.stdout.flush()


def multi_line_progress(write_progress, tasks):
    # Move the cursor back up to overwrite the previous progress state
    sys.stdout.write("\033[F" * len(tasks))

    # Print each task with its progress bar on a new line
    for task, progress in tasks.items():
        write_progress(task, progress)
        print()  # New line for each task
    sys.stdout.flush()
