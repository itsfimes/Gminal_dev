from utils.print_utils import print
import sys
import importlib
import os
from colorama import Fore

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def _parse(core, command: str) -> None:
    command = command.strip()

    # safely evaluate expressions in core + globals
    def eval_expr(expr: str):
        core_vars = {k: getattr(core, k) for k in dir(core) if not k.startswith("_")}
        context = {**core_vars, **globals()}
        try:
            # Detect f-string literals
            if expr.startswith("f") and (expr[1:].startswith('"') or expr[1:].startswith("'")):
                # Use eval with added context, allowing interpolation :>
                return eval(expr, {"__builtins__": None}, context)
            else:
                return eval(expr, {"__builtins__": None}, context)
        except Exception:
            raise

    def resolve_name(name: str):
        parts = name.split(".")
        first_part = parts[0]
        vars = core.get_vars()
        print(str(parts), condition=core.debug_mode)

        # 1. Try globals() first :3
        print(f"Globals resolve for {first_part}", condition=core.debug_mode)
        obj = vars.get(first_part, getattr(core, first_part, None))

        # 2. Then try core if available
        if obj is None and 'core' in globals():
            print(f"Core resolve for {first_part}", condition=core.debug_mode)
            obj = getattr(globals()['core'], first_part, None)

        # 3. Try importing module from project directory
        if obj is None and first_part != "":
            print(f"Project directory resolve for {first_part}", condition=core.debug_mode)
            sys.path.insert(0, PROJECT_DIR)
            try:
                obj = importlib.import_module(first_part)
            except ModuleNotFoundError:
                obj = None
            finally:
                sys.path.pop(0)

        if obj is None:
            print(f"{name} NONE'd", condition=core.debug_mode)
            return None

        # Resolve attributes safely :p
        print(f"Resolving attributes for {name}", condition=core.debug_mode)
        for part in parts[1:]:
            if not hasattr(obj, part):
                print("Invalid attribute")
                return None
            obj = getattr(obj, part)
        
        print(f"{Fore.GREEN} - Done ><", condition=core.debug_mode, same_line_print=True)
        return obj

    if command == "core-shell":
        core.enqueue_command(command)
        core.process_queue()
        return

    try:

        # assignment: var = expr
        if "=" in command:
            var_location, expr_str = command.split("=", 1)
            var_location = var_location.strip()
            expr_str = expr_str.strip()

            value = None

            # handle function calls in assignments: e.g. x = utils.gres_parser.GresParser(core)
            if "(" in expr_str and expr_str.endswith(")"):
                func_name, args_str = expr_str.split("(", 1)
                func_name = func_name.strip()
                args_str = args_str[:-1].strip()

                func = resolve_name(func_name)
                if func and callable(func):
                    args = []
                    if args_str:
                        for raw_arg in args_str.split(","):
                            raw_arg = raw_arg.strip()
                            try:
                                arg = eval_expr(raw_arg)
                            except Exception:
                                arg = resolve_name(raw_arg)
                            args.append(arg)
                    value = func(*args)
                else:
                    print(f"Unknown function in assignment: {func_name}... :c")
                    return
            else:
                # normal expression or variable resolution
                try:
                    value = eval_expr(expr_str)
                except Exception:
                    value = resolve_name(expr_str)

            # assign value to proper location
            if "." in var_location:
                var_name = var_location.split(".")[-1]
                parent = resolve_name(".".join(var_location.split(".")[:-1]))
                if parent is not None:
                    setattr(parent, var_name, value)
                else:
                    print(f"Unknown target object: {var_location}")
            else:
                setattr(core, var_location, value)

            print(f"Set {var_location} = {value}", condition=core.debug_mode)
            return

        # function call: func(args)
        if "(" in command and command.endswith(")"):
            func_name, args_str = command.split("(", 1)
            func_name = func_name.strip()
            args_str = args_str[:-1].strip()
            func = resolve_name(func_name)

            if func and callable(func):
                args = []
                if args_str:
                    for raw_arg in args_str.split(","):
                        raw_arg = raw_arg.strip()
                        try:
                            arg = eval_expr(raw_arg)
                        except Exception:
                            arg = resolve_name(raw_arg)
                        args.append(arg)
                func(*args)
            else:
                print(f"Unknown function: {func_name}... :c")
            return

        # fallback 
        func = resolve_name(command)
        if func:
            if callable(func):
                func()
            else:
                print(f"{command} isn't callable x.x")
            return

        print("Invalid command format :c")
    except Exception as e:
        print(f"Error parsing command: {e}")


def parse(core, command: str) -> None:
    _parse(core, command)
