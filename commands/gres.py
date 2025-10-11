# A command interface for Gminal's script lang :3
from utils.gres_parser import GresParser

def execute(core, file: str):
    GresParser(core).execute_commands(file)
