import ctypes
import queue
import importlib
import os
from utils.print_utils import print
import colorama
from colorama import Fore, Back, Style
from pathlib import Path

colorama.init(autoreset=True)


class CoreFunctionality:
    def __init__(self):
        self.core_version = "0.0.7"
        self.task_queue = queue.Queue()  # Queue to manage tasks
        self.commands = {}
        self.root_access = None
        self.check_root()
        self.welcome_text = Fore.LIGHTCYAN_EX + r"""
           ______               __                   __ 
          /      \             |  \                 |  \
         |  ▓▓▓▓▓▓\______ ____  \▓▓_______   ______ | ▓▓
         | ▓▓ __\▓▓      \    \|  \       \ |      \| ▓▓
         | ▓▓|    \ ▓▓▓▓▓▓\▓▓▓▓\ ▓▓ ▓▓▓▓▓▓▓\ \▓▓▓▓▓▓\ ▓▓
         | ▓▓ \▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓/      ▓▓ ▓▓
         | ▓▓__| ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓  ▓▓▓▓▓▓▓ ▓▓
          \▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓ ▓▓  | ▓▓\▓▓    ▓▓ ▓▓
           \▓▓▓▓▓▓ \▓▓  \▓▓  \▓▓\▓▓\▓▓   \▓▓ \▓▓▓▓▓▓▓\▓▓
                                                        
    """
        self.startingdir = os.getcwd()
        self.homedir = Path.home()
        self.debug_mode = False

    def load_commands(self, commands_dir='commands', silent=False):
        """Dynamically load commands from the specified directory."""
        for file in os.listdir(commands_dir):
            if file.endswith('.py'):
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f'{commands_dir}.{module_name}')
                    if hasattr(module, 'execute'):
                        self.commands[module_name] = module.execute
                        if not silent:
                            print(f"Command '{module_name}' loaded successfully.")
                except Exception as e:
                    print(f"Failed to load command '{module_name}': {e}")

    def enqueue_command(self, command_name, *args):
        """Add a command to the task queue."""
        if command_name in self.commands:
            self.task_queue.put((command_name, args))
            # print(f"Command '{command_name}' enqueued with args: {args}")
        else:
            print(f"Command '{command_name}' not found. Please check the available commands.")

    def process_queue(self):
        """Process and execute commands from the task queue."""
        while not self.task_queue.empty():
            command_name, args = self.task_queue.get()
            if not self.debug_mode:
                try:
                    # print(f"Executing '{command_name}'...")
                    # Call the command, passing 'self' as the first argument
                    self.commands[command_name](self, *args)
                except Exception as e:
                    print(f"Error while executing '{command_name}': {e}")
            else:
                print(f"Executing {command_name} ({self.commands[command_name]}) with {args}")
                self.commands[command_name](self, *args)

    def quit_gminal(self):
        self.task_queue = None  # Just nukes the queue, might cause issues down the line, but it should be just fine for now.
        quit(0)

    def check_root(self):
        try:
            self.root_access = (os.getuid() == 0)
        except AttributeError as e:
            self.root_access = ctypes.windll.shell32.IsUserAnAdmin() != 0

    def get_is_root(self):
        return self.root_access


# Test, also makes my IDE not complain, about this file having no output, when executed
if __name__ == "__main__":
    core = CoreFunctionality()
    core.load_commands()
    core.enqueue_command('example_command', 'arg1', 'arg2')
    core.process_queue()
