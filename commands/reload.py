# Reloads commands
import os
import sys
import importlib
import site

# get all site-packages paths so we can skip them
site_paths = site.getsitepackages()

def is_local_module(module):
    path = getattr(module, "__file__", None)
    if not path:
        return False
    # skip anything inside site-packages or stdlib
    if any(path.startswith(sp) for sp in site_paths):
        return False
    if path.startswith(sys.base_prefix):  # stdlib path
        return False
    return os.path.isfile(path)

def reload_local_modules():
    for name, module in list(sys.modules.items()):
        if module and is_local_module(module):
            try:
                importlib.reload(module)
                print(f"Reloaded {name}")
            except Exception as e:
                print(f"Could not reload {name}: {e}")


def execute(core):
    core.commands = {}
    old_dir = os.getcwd()
    os.chdir(core.startingdir)
    core.load_commands()
    os.chdir(old_dir) #  has to be done this way until i fix loading commands in core :p
    # reload_local_modules() -- too unstable, will be added soon tho :p

