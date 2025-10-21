# Override the built-in print function with our custom one, yes I know this is cursed
import builtins
import sys
import os
from tqdm import tqdm
from typing import Any

def print(message: Any = "", 
          style: str = "", 
          condition: bool = True,
          same_line_print: bool = False):
    """the thingy that prints stuff :3
        - styles: **bold**, <u>underline</u> (default = '')
        - condition: A bool that must be true for text to print (default = True)
        - same_line_print: whether to print the text to the same line"""

    # initialize persistent attribute on first use :3
    if not hasattr(print, "last_message_length"):
        print.last_message_length = 0 # type: ignore[attr-defined] - (make pyright and other lsps shut up about this definitely not cursed coding masterpiece)

    message = str(message)

    if condition:
        match style:
            case "bold":
                message = f"\033[1m{message}\033[0m"
            case "underline":
                message = f"\033[4m{message}\033[0m"

        if same_line_print:
            if print.last_message_length > 0: # type: ignore[attr-defined]
                sys.stdout.write("\033[F")  # move up one line # type: ignore[attr-defined]
                sys.stdout.write(f"\033[{print.last_message_length}C")  # move cursor right # type: ignore[attr-defined]
                sys.stdout.write(message + "\n")
            sys.stdout.flush()
        else:
            builtins.print(message)

        # update persistent value :3
        print.last_message_length = len(message) # type: ignore[attr-defined]

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

def print_list_in_columns(data, items_per_row=5):
    for i in range(0, len(data), items_per_row):
        print(" ".join(f"{item:<15}" for item in data[i:i+items_per_row]))
