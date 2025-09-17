# Switches debug mode for core
from utils.modifier_stack import Modifier
from colorama import Fore

def execute(core):
    core.debug_mode = True if not core.debug_mode else False
    if core.debug_mode:
        core.debugger.activate()
        core.modifier.activate(Modifier("debug.execute()", "debug", "core.debug", Fore.RED))
    else:
        core.debugger.deactivate()
        core.modifier.deactivate("core.debug")
 
