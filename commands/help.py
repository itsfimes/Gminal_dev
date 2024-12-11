# For right now just displays commands
from utils.print_utils import print_list_in_columns
cmds = []

def execute(core):
    for command in core.commands:
        cmds.append(command)
    print_list_in_columns(cmds)