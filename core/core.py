import ctypes
import queue
import importlib
import os
from utils.print_utils import print, tqdm_bar
import colorama
from colorama import Fore, Back, Style
from pathlib import Path
import shutil
import subprocess

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
            """Dynamically load Python commands and system commands."""
            # Load Python-based commands
            for file in os.listdir(commands_dir):
                if file.endswith('.py'):
                    module_name = file[:-3]
                    if not self.debug_mode:
                        try:
                            module = importlib.import_module(f'{commands_dir}.{module_name}')
                            if hasattr(module, 'execute'):
                                self.commands[module_name] = module.execute
                                if not silent:
                                    print(f"Command '{module_name}' loaded successfully.")
                        except Exception as e:
                            print(f"Failed to load command '{module_name}': {e}")
                    else:
                        module = importlib.import_module(f'{commands_dir}.{module_name}')
                        if hasattr(module, 'execute'):
                            self.commands[module_name] = module.execute
                            if not silent:
                                print(f"Command '{module_name}' loaded successfully.")

            # Load system commands
            paths = os.environ.get("PATH", "").split(os.pathsep)
            total_files = sum(len(os.listdir(path_dir)) for path_dir in paths if os.path.isdir(path_dir))

            progress_bar = tqdm_bar(total=total_files, disable=silent, desc="Registering System Commands", unit="cmd")
            
            for path_dir in paths:
                if not os.path.isdir(path_dir):
                    continue

                for cmd in os.listdir(path_dir):
                    progress_bar.update(1)
                    if cmd not in self.commands and shutil.which(cmd):
                        self.commands[cmd] = self._create_system_command(cmd)
            
            progress_bar.close()

    def _create_system_command(self, cmd):
        """Wrap a system command as a callable function."""
        def command_executor(manager, *args):
            try:
                #result = subprocess.run([cmd, *args], check=True, text=True, capture_output=True)
                #print(result.stdout)
                try:
                    command_args = " ".join([cmd, *args])
                except TypeError as e:
                    if self.debug_mode:
                        print(e)
                    command_args = ""
                if self.debug_mode:
                    print(f"{command_args}")
                os.system(f"{command_args}")
            except subprocess.CalledProcessError as e:
                print(f"Error executing '{cmd}': {e.stderr}")
        return command_executor

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
