# Reloads commands
import os


def execute(core):
    core.commands = {}
    old_dir = os.getcwd()
    os.chdir(core.startingdir)
    core.load_commands()
    os.chdir(old_dir)
