import readline

class CommandCompletion:
    def __init__(self, commands):
        self.commands = commands
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    def complete(self, text, state):
        matches = [cmd for cmd in self.commands if cmd.startswith(text)]
        return matches[state] if state < len(matches) else None
