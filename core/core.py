import ctypes
from queue import Queue
import importlib
import os
from utils.print_utils import print, tqdm_bar
from utils.su_manager import SuperUserManager
from utils.modifier_stack import ModifierStack 
from utils.decorators import decorate_all_methods
from utils.debug import GminalCoreDebugger
import colorama
from colorama import Fore
from pathlib import Path
import shutil

colorama.init(autoreset=True)

debugger = GminalCoreDebugger()

@decorate_all_methods(debugger.debug_decorator)
class CoreFunctionality:
    def __init__(self):
        self.core_version: str = "0.0.8"
        self.task_queue: Queue = Queue()  # Queue to manage tasks
        self.commands: dict = {}
        self.root_access: bool = False # placeholder
        self.check_root() # overwrite root_access placeholder
        self.welcome_text: str = Fore.LIGHTCYAN_EX + r"""
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
        self.startingdir: str = os.getcwd()
        self.homedir = Path.home()

        self.debug_mode: bool = False
        self.debugger = debugger

        self.core_shell: bool = False
        
        self.su_man = SuperUserManager(self)
        
        self.parser_type: str = "default"
        self.command_parser = None
        self.modifier = ModifierStack()  # thingy that keeps track of current shell modifiers like debug mode :3
        
        self.host_running: bool = False  # controlled by the host component(usually a cli) :3
                                    # False until the host component sets it to True - indicating that it finished init
        
        # Attach debugger to core
        self.debugger.attach_core(self)

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
                        print(f"{commands_dir}.{module_name}")
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
        def execute(core, # here cuz executor expects it
                    *args):
            command_args = " ".join([cmd, *args])
            print(f"{command_args}", condition=self.debug_mode)
            os.system(f"{command_args}")
        return execute

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

    def quit_gminal(self, let_host_terminate: bool = False):
        self.host_running = False
        if not let_host_terminate:
            quit(0)

    def check_root(self):
        try:
            self.root_access = (os.getuid() == 0)
        except AttributeError:
            self.root_access = ctypes.windll.shell32.IsUserAnAdmin() != 0

    def get_is_root(self):
        return self.root_access

    def get_vars(self):
        # TODO: Implement getting interface vars
        access = self.su_man.sudo_check()
        if access:
            return globals().copy(), {key: value for key, value in self.__dict__.items() if key != "commands"}
        else:
            return "Superuser check failed for getting core variables"
