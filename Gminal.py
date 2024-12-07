from core.core import CoreFunctionality
from utils.print_utils import print, clean_screen
import colorama
from colorama import Fore, Back, Style
import os
import argparse

parser = argparse.ArgumentParser(prog="Gminal Core V2")
parser.add_argument("--before-load-dir", type=str, help="Sets what directory to cd into before start, usually the directory, that you have Gminal installed in")
parser.add_argument("--after-load-dir", type=str, help="Sets what directory to cd into after start")
args = parser.parse_args()

after_load_dir = args.after_load_dir
before_load_dir = args.before_load_dir


colorama.init(autoreset=True)

version = "0.0.7"


def main():
    print(before_load_dir)
    if before_load_dir is not None:
        os.chdir(before_load_dir)
    # Initialize core functionality
    print("Getting core")
    core = CoreFunctionality()
    print("Loading commands")
    core.load_commands(silent=True)
    print(f"Welcome to {Fore.LIGHTCYAN_EX} Gminal{Fore.RESET}!")
    print(after_load_dir)
    if after_load_dir is not None:
        os.chdir(after_load_dir)  # Chage the dir into provided directory, if it's provided
    def get_core():
        return core

    clean_screen()
    print(core.welcome_text)
    print(f"    | CLI version {Fore.CYAN} {version}")
    print(f"    | Core version: {Fore.CYAN} {core.core_version}")
    print(f"    | Made with love and caffeine by " + Fore.LIGHTBLUE_EX + "@ItzFimes")
    print("\n")

    while True:
        shellicon = "# " if core.root_access else "$ "
        debug_mode_icon = f"{Fore.RED}|debug| {Fore.RESET}" if core.debug_mode else ""
        if os.getcwd() == str(core.homedir):
            terminalico = f"{debug_mode_icon}{Fore.CYAN}~{Fore.RESET} {shellicon}"
        else:
            terminalico = f"{debug_mode_icon}{Fore.CYAN}{os.getcwd()}{Fore.RESET} {shellicon}"
        try:
            user_input = input(f"{terminalico}").strip()
        except KeyboardInterrupt:
            print("\n Exiting Gminal. Goodbye :3")
            core.quit_gminal()
            break
        if user_input.lower() == 'exit':
            print("Exiting Gminal. Goodbye :3")
            core.quit_gminal()
            break  # this code is here just in case something fails in the core, while quiting

        # Parse the user input
        command_parts = user_input.split()
        if command_parts:
            command_name = command_parts[0]
            args = command_parts[1:]

            # Enqueue and process the command using core
            core.enqueue_command(command_name, *args)
            core.process_queue()  # Immediate processing for simplicity


if __name__ == "__main__":
    main()
