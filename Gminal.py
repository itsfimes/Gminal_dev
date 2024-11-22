from core.core import CoreFunctionality
from utils.print_utils import print, clean_screen
import colorama
from colorama import Fore, Back, Style
import os

colorama.init(autoreset=True)

version = "0.0.7"


def main():
    # Initialize core functionality
    core = CoreFunctionality()
    core.load_commands()

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
        if os.getcwd() == str(core.homedir):
            terminalico = f"{Fore.CYAN}~{Fore.RESET} {shellicon}"
        else:
            terminalico = f"{Fore.CYAN}{os.getcwd()}{Fore.RESET} {shellicon}"
        user_input = input(f"{terminalico}").strip()
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
