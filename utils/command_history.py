import readline
from pathlib import Path

class CommandHistory:
    def __init__(self, history_file='command_history/gminal_history.txt'):
        self.history_file = Path(history_file)
        self.load_history()

    def load_history(self):
        if self.history_file.exists():
            readline.read_history_file(self.history_file)

    def save_history(self):
        readline.write_history_file(self.history_file)
