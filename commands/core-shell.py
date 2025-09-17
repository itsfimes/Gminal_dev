# Allows for user access into the core
from utils.parser_loader import load_command_parser
from utils.modifier_stack import Modifier
from colorama import Fore

def execute(core):
    core.core_shell = True if not core.core_shell else False
    core.parser_type = "core_shell" if not core.parser_type == "core_shell" else "default"
    if core.core_shell:
        core.modifier.activate(Modifier("core-shell.execute()", "core shell", "utils.core-shell", Fore.LIGHTCYAN_EX))
    else:
        core.modifier.deactivate("utils.core-shell")
    load_command_parser(core)
