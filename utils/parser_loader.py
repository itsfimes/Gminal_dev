import importlib.util
import os
import sys

def load_command_parser(core):
    parser_type = core.parser_type
    parser_path = os.path.join(core.startingdir, "utils", "command_parsers", f"{parser_type}.py")

    if not os.path.isfile(parser_path):
        raise FileNotFoundError(f"Command parser '{parser_type}' not found at {parser_path} >~<")

    module_name = f"command_parser_{parser_type}"
    spec = importlib.util.spec_from_file_location(module_name, parser_path)
    if spec is None:
        raise ImportError(f"Failed to create spec for {parser_path} :<")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    core.command_parser = module
