# Debugger decorator and other stuff :3
from utils.print_utils import print
from utils.datatypes import CoreDebuggerDatatype 
from colorama import Fore

class GminalCoreDebugger:
    def __init__(self) -> None:
        self.core = None
        self.ready: bool = False  # flag to signal if core is attached to debugger ><
        self.active: bool = False

    def attach_core(self, core: CoreDebuggerDatatype):
        self.core = core
        self.ready = True
        print("Debugger attached to core :3", condition=not core.host_controller.silent_startup)
    
    def activate(self):
        if self.ready:
            self.active = True
        else:
            raise Exception(f"{Fore.RED}Failed{Fore.RESET} to activate debbuger: core is not attached to debugger")
    
    def deactivate(self):
        if self.active:
            self.active = False
        else:
            print("Debbuger already deactivated")

    def debug_decorator(self, func):
        def wrapper(*args, **kwargs):
            print(f"Calling {Fore.LIGHTCYAN_EX}{func.__name__}{Fore.RESET} >< (args: {args if args else 'None :p'} -- kwargs: {kwargs if kwargs else 'None :p'})",
                  condition=self.active)
            result = func(*args, **kwargs)
            print(f"{Fore.GREEN}{func.__name__}{Fore.RESET} finished :3", condition=self.active)
            return result
        return wrapper
