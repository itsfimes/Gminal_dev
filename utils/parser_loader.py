from typing import cast
import importlib.util
import os
import sys
from utils.datatypes import ParserDatatype, GminalCoreParserDatatype

# Avoid cyclical imports :p
def get_starting_dir():
    from core.core import get_starting_dir as _real_get_starting_dir
    return _real_get_starting_dir()


def get_command_parser(path: str, name: str) -> ParserDatatype:
    """Returns a parser module that has a parse() function ><"""

    parser_path = path
    parser_type = name

    if not os.path.isfile(parser_path):
        raise FileNotFoundError(f"Command parser not found at {parser_path} >~<")

    module_name = f"command_parser_{parser_type}"
    spec = importlib.util.spec_from_file_location(module_name, parser_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to create spec for {parser_path} :<")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)  # type: ignore[union-attr]

    # runtime check
    if not hasattr(module, "parse") or not callable(module.parse):
        raise TypeError(f"Loaded module {module_name} does not implement ParserDatatype \n fix: add a parse() function to your parser :c")

    return cast(ParserDatatype, module)

def load_command_parser(core: GminalCoreParserDatatype):
    """Loads a command parser into core :3"""

    parser_type: str = core.parser_type
    parser_path: str = get_parser_path(parser_type)

    parser = get_command_parser(parser_path, parser_type)
    
    core.command_parser = parser

def get_parser_path(name: str):
    return os.path.join(get_starting_dir(), "utils", "command_parsers", f"{name}.py")
