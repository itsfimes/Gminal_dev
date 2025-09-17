import readline
import os
from pathlib import Path

class CommandCompletion:
    def __init__(self, commands, history_file='command_history/gminal_history.txt'):
        self.commands = commands
        self.history_file = Path(history_file)
        self.load_history()
        
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    def load_history(self):
        if self.history_file.exists():
            try:
                readline.read_history_file(self.history_file)
            except Exception:
                pass  # Ignore errors if the history file is empty or corrupted

    def get_history_matches(self, text):
        matches = []
        for i in range(readline.get_current_history_length()):
            entry = readline.get_history_item(i + 1)
            if entry and entry.startswith(text) and entry not in matches:
                matches.append(entry)
        return matches

    def complete(self, text, state):
        matches = []

        # Command completions
        matches.extend([cmd for cmd in self.commands if cmd.startswith(text)])

        # File completions (supports full/partial paths)
        expanded = os.path.expanduser(text)
        dir_part, partial = os.path.split(expanded)
        if dir_part == "":
            dir_part = "."  # Use current directory if no path part

        try:
            files = os.listdir(dir_part)
            for f in files:
                if f.startswith(partial):
                    full_path = os.path.join(dir_part, f)
                    if os.path.isdir(full_path):
                        full_path += os.sep
                    # Reconstruct with original user tilde if needed
                    display_path = os.path.join(text[:text.rfind(partial)], f)
                    matches.append(display_path)
        except Exception:
            pass  # Ignore invalid paths

        # History completions
        matches.extend(self.get_history_matches(text))

        return matches[state] if state < len(matches) else None
