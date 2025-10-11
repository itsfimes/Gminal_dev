from queue import Queue
import importlib
import os
from utils.print_utils import print, tqdm_bar
from utils.su_manager import SuperUserManager
from utils.modifier_stack import ModifierStack 
from utils.decorators import decorate_all_methods
from utils.debug import GminalCoreDebugger
from utils.datatypes import GresParserCoreDatatype, HostCoreDatatype
from utils.gres_parser import GresParser
import colorama
from colorama import Fore
from pathlib import Path
import shutil
from typing import Any

colorama.init(autoreset=True)

debugger = GminalCoreDebugger()

class PlaceholderClass:
    pass


def get_starting_dir() -> str:
    """A way to get startingdir without attaching to core"""

    return str(Path(__file__).resolve().parents[1])

@decorate_all_methods(debugger.debug_decorator)
class CoreFunctionality:
    def __init__(self, host_controller: HostCoreDatatype) -> None:
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
        self.command_parser: Any = PlaceholderClass()
        self.modifier = ModifierStack()  # thingy that keeps track of current shell modifiers like debug mode :3
        
        self.host_running: bool = False  # controlled by the host component(usually a cli) :3
                                         # False until the host component sets it to True - indicating that it finished init
        self.host_controller: HostCoreDatatype = host_controller # empty until a host component gets attached :3
        
        # own gres parser instance so we don't have to borrow from a host :p 
        self.gres_parser: GresParserCoreDatatype = GresParser(self) 

        # Attach debugger to core
        self.debugger.attach_core(self)
    

    def load_commands(self, commands_dir='commands', silent=False) -> None:
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

    def _create_system_command(self, cmd: str):
        """Wrap a system command as a callable function."""
        def execute(core, # here cuz executor expects it
                    *args):
            command_args = " ".join([cmd, *args])
            print(f"{command_args}", condition=self.debug_mode)
            os.system(f"{command_args}")
        return execute

    def enqueue_command(self, command_name, *args) -> None:
        """Add a command to the task queue."""
        if command_name in self.commands:
            self.task_queue.put((command_name, args))
            # print(f"Command '{command_name}' enqueued with args: {args}")
        else:
            print(f"Command '{command_name}' not found. Please check the available commands.")


    def process_queue(self) -> None:
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

    def quit_gminal(self, let_host_terminate: bool = False) -> None:
        self.host_running = False
        print("Running exit scripts", condition=not self.host_controller.silent_exit)
        self.gres_parser.execute_commands(f"{self.startingdir}/conf/exit.gres")
        if not let_host_terminate:
            quit(0)

    def check_root(self) -> None:
        """Update core's root flag :>"""
        self.root_access = (os.getuid() == 0)

    def get_is_root(self) -> bool:
        return self.root_access

    def get_vars(self) -> dict[str, Any]:
        # TODO: Implement getting module vars
        return {**globals().copy(), **{key: value for key, value in self.__dict__.items() if key != "commands"}}

    def get_core(self):
        return self
    
    def add_module(self, module_name: str) -> None:
        try:
            print(f"Importing {module_name}")
            module = importlib.import_module(module_name)
            globals()[module_name] = module 
            print(f"{Fore.GREEN} - Done :3", same_line_print=True)
        except ModuleNotFoundError:
            print(f"Module '{module_name}' not found :c")


