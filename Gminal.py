from core.core import CoreFunctionality
from utils.print_utils import print, clean_screen
import colorama
from colorama import Fore
import os
import argparse
from utils.command_completion import CommandCompletion
from utils.command_history import CommandHistory
from utils.parser_loader import load_command_parser
from utils.shellinput_constructor import ShellInputConstructor
import atexit

parser = argparse.ArgumentParser(prog="Gminal.py")
parser.add_argument("--before-load-dir", type=str, help="Sets what directory to cd into before start")
parser.add_argument("--after-load-dir", type=str, help="Sets what directory to cd into after start")
parser.add_argument("--wait-after-init", action="store_true", help="Waits for enter to be pressed after all modules and core have been initialized")
parser.add_argument("--no-welcome", action="store_true", help="Doesn't show welcome text on startup")
parser.add_argument("--silent-startup", action="store_true", help="Disables startup logs")
parser.add_argument("--silent-exit", action="store_true", help="Disables the cute exit message")
args = parser.parse_args()

after_load_dir = args.after_load_dir
before_load_dir = args.before_load_dir
wait_after_init = args.wait_after_init
no_welcome_text = args.no_welcome
silent_startup = args.silent_startup
silent_exit = args.silent_exit


colorama.init(autoreset=True)

version = "0.0.8"


def main():
    print(before_load_dir, condition=not silent_startup)
    if before_load_dir is not None:
        os.chdir(before_load_dir)

    # Initialize core functionality
    print("Getting core", condition=not silent_startup)
    core = CoreFunctionality()

    print("Loading commands", condition=not silent_startup)
    core.load_commands(silent=True)

    print("Loading interface components", condition=not silent_startup)
    CommandCompletion(commands=core.commands.keys())
    historian = CommandHistory(core.startingdir, history_file=f"{core.startingdir}/utils/command_history/history.gres")
    shell_input_constructor = ShellInputConstructor(core)
    atexit.register(historian.save_history)  # Using atexit since there's currently no global exit flag implementation
    
    print("Loading parser", condition=not silent_startup)
    load_command_parser(core)

    print(f"Welcome to {Fore.LIGHTCYAN_EX}Gminal{Fore.RESET}!", condition=not silent_startup)
    
    print("Arming main loop core flag - core.host_running")
    core.host_running = True

    print(after_load_dir, condition=not silent_startup)
    if after_load_dir is not None:
        os.chdir(after_load_dir)  # Chage the dir into provided directory, if it's provided

    if wait_after_init:
        input("Waiting after init due to the --wait-after-init flag being passed \nPress enter to continue")
    if not no_welcome_text:
        clean_screen()
        print(core.welcome_text)
        print(f"    | CLI version {Fore.CYAN} {version}")
        print(f"    | Core version {Fore.CYAN} {core.core_version}")
        print("\n")

    while core.host_running:
        terminalico = shell_input_constructor.construct_shell_input(f"{core.startingdir}/shellinput.conf")
        try:
            user_input = input(f"{terminalico}").strip()
        except KeyboardInterrupt:
            print("\n Exiting Gminal. Goodbye :3", condition=not silent_exit)
            core.quit_gminal()
        except EOFError:
            print(f"EOFQUIT - {Fore.RED}core.quit_gminal won't be executed!{Fore.RESET}")
            print("Goodbye :3")
            quit()
        if user_input.lower() == 'exit':
            print("Exiting Gminal. Goodbye :3", condition=not silent_exit)
            core.quit_gminal()

        # Parse the user input
        try:
            core.command_parser.parse(core, user_input)
        except Exception as e:
            print(f"Error occured after or while parsing >~< {Fore.RED}{e}{Fore.RESET}")

if __name__ == "__main__":
    main()
