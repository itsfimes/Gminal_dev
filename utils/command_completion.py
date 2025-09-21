import readline
import os

class CommandCompletion:
    def __init__(self, commands=None, enable_path_completion=True):
        self.commands = commands or []
        self.enable_path_completion = enable_path_completion
        self.matches = []

        delimiters = readline.get_completer_delims()
        delimiters = delimiters.replace("/", "").replace("-", "")
        readline.set_completer_delims(delimiters)

        readline.set_completer(self._complete)
        readline.parse_and_bind("tab: complete")

    def _complete(self, text, state):
        """
        The thingy that generates the completions :3
        """
        # check if we're completing a path :3
        if self.enable_path_completion and ("/" in text or text.startswith(".")):
            return self._complete_path(text, state) # when completing paths only return paths and files as matches ><

        # only generate matches if this is the first time this text has been here :3
        elif state == 0:
            self.matches = [cmd for cmd in self.commands if cmd.startswith(text)]
            self.matches.append(self.check_for_files(text)) # include files in command matches :3

        return self.matches[state] if state < len(self.matches) else None

    def _complete_path(self, text, state):
        """
        Generate completions for paths ><
        """
        # expand user (~) and get directory + partial filename
        expanded = os.path.expanduser(text)
        dirname = os.path.dirname(expanded) or "."
        prefix = os.path.basename(expanded)

        try:
            files = os.listdir(dirname)
        except FileNotFoundError:
            return None
        matches = []
        for f in files:
            if f.startswith(prefix):
                full_path = os.path.join(dirname, f)
                # add trailing slash for directories :>
                if os.path.isdir(full_path):
                    f += "/"
                matches.append(os.path.join(os.path.dirname(text) or "", f))

        matches.sort()
        return matches[state] if state < len(matches) else None
    
    def check_for_files(self, text):
        for file in os.listdir():
            if file.startswith(text):
                return file
        
        return None
