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

colorama.init(autoreset=True)


version = "0.0.8"

class GminalCli:
    def __init__(self, init_args) -> None:
        print("Setting variables")
        self.ok_message = f"{Fore.GREEN} - Done"

        # ik that loading these can be done dynamically, 
        # but im afraid of accidentaly overwriting variables when i add more args :p 
        self.after_load_dir = init_args.after_load_dir
        self.before_load_dir = init_args.before_load_dir
        self.wait_after_init = init_args.wait_after_init
        self.no_welcome_text = init_args.no_welcome
        self.silent_startup = init_args.silent_startup
        self.silent_exit = init_args.silent_exit
        self.print_done()

        print(f"Init dir: {self.before_load_dir}", condition=not self.silent_startup)
        if self.before_load_dir is not None:
            os.chdir(self.before_load_dir)

        # Initialize core functionality
        print("Getting core", condition=not self.silent_startup)
        self.core = CoreFunctionality()
        self.core.host_controller = self
        self.print_done()

        print("Loading commands", condition=not self.silent_startup)
        self.core.load_commands(silent=True)
        self.print_done()

        print("Loading interface components", condition=not self.silent_startup)
        CommandCompletion(commands=self.core.commands.keys(), enable_path_completion=True)
        os.makedirs(f"{self.core.startingdir}/utils/command_history", exist_ok=True)  # make sure that history dir exists :3
        self.historian = CommandHistory(f"{self.core.startingdir}/utils/command_history/gminal_history.txt")
        atexit.register(self.historian.save_history)  # Using atexit since there's currently no global exit flag implementation
        self.shell_input_constructor = ShellInputConstructor(self.core)
        self.print_done() 

        print("Loading parser", condition=not self.silent_startup)
        load_command_parser(self.core)
        self.print_done()


        print(f"Welcome to {Fore.LIGHTCYAN_EX}Gminal{Fore.RESET}!", condition=not self.silent_startup)
        

        print(f"Post-init dir: {self.after_load_dir}", condition=not self.silent_startup)
        if self.after_load_dir is not None:
            os.chdir(self.after_load_dir)  # Chage the dir into provided directory, if it's provided

        print("init -> interactive_shell handoff", condition=not self.silent_startup)
        self.interactive_shell()


    
    def interactive_shell(self) -> None:
        self.print_done() # interactive_shell handoff done :3

        print("Arming main loop core flag - core.host_running")
        self.core.host_running = True
        self.print_done()

        if self.wait_after_init:
            input("Waiting after init due to the --wait-after-init flag being passed \nPress enter to continue")
        if not self.no_welcome_text:
            clean_screen()
            print(self.core.welcome_text)
            print(f"    | CLI version {Fore.CYAN} {version}")
            print(f"    | Core version {Fore.CYAN} {self.core.core_version}")
            print("\n")
        
        user_input: str = "" # Avoid lsp unbound warnings :p
        while self.core.host_running:
            terminalico = self.shell_input_constructor.construct_shell_input(f"{self.core.startingdir}/shellinput.conf")
            try:
                user_input = input(f"{terminalico}").strip()
            except KeyboardInterrupt:
                print("\n Exiting Gminal. Goodbye :3", condition=not self.silent_exit)
                self.core.quit_gminal()
            except EOFError:
                print(f"EOFQUIT - {Fore.RED}core.quit_gminal won't be executed!{Fore.RESET}")
                print("Goodbye :3")
                quit()
            if user_input.lower() == "exit":
                print("Exiting Gminal. Goodbye :3", condition=not self.silent_exit)
                self.core.quit_gminal()

            # Parse the user input
            try:
                self.core.command_parser.parse(self.core, user_input)
            except Exception as e:
                print(f"Error occured after or while parsing >~< {Fore.RED}{e}{Fore.RESET}")

    def print_done(self) -> None:
        print(self.ok_message, condition=not self.silent_startup or not self.silent_exit, same_line_print=True)

if __name__ == "__main__":
    GminalCli(args)
