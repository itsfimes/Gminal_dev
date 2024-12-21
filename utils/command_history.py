import readline
from pathlib import Path
import os

class CommandHistory:
    def __init__(self, startingdir, history_file='command_history/gminal_history.txt'):
        self.history_file = Path(history_file)
        if not os.path.exists(self.history_file):
            os.makedirs(f"{startingdir}/utils/command_history")
            with open(self.history_file, "x"):
                pass
        self.load_history()

    def load_history(self):
        if self.history_file.exists():
            readline.read_history_file(self.history_file)

    def save_history(self):
        readline.write_history_file(self.history_file)
