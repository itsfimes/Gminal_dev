# the thingy that constructs what the shell input looks like :3

import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)


CONFIG_FILE: str = "shellinput.conf"
HELP_TEXT: str = """# Configuration for ShellInputConstructor
# This file only configures how the shell input looks like, not the actual process of creating the shell input
# the syntax for this file is quite simple and follows these simple rules :3
#  - each line starting with a hashtag is ignored
#  - every config parameter must be separated using `|`
#  - newlines are ignored when constructing the shell input, so your config *can* be split into multiple lines but it may have negative impacts on performance if you overdo it
#  - invalid parameters will just end up as text
#
# CONFIG PARAMETERS ><
#   - shellstatus // current shell modifications like debug mode and core-shell
#   - path // current path, `~` if current dir == Path.home()
#   - shellicon // `$` if running as a normal user, `#` if running as root

# colors and more parameters coming soon :3
"""

class ShellInputConstructor():
    def __init__(self, 
                 core,
                 config_file: str = CONFIG_FILE,):

        self.config_file: str = config_file
        self.config: str = ""
        self.core = core

    def create_default_config(self) -> None:
        print("Creating default config for shellinput! :3")
        with open(self.config_file, "w+") as f:
            f.write(HELP_TEXT)
            f.write("shellstatus|path| |shellicon")

    def load_config(self) -> str:
        """Return a parsed version of the config 
           that is one line and without comments"""

        if not os.path.exists(self.config_file):
            self.create_default_config()
        
        # parse config into one line and get rid of comments
        config_list: list[str] = []
        with open(self.config_file, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                config_list.append(line.strip())

        return "".join(config_list) # return config as a string without comments
    def get_config(self) -> None:
        """Wrapper for load_config to update class config info"""
        self.config = self.load_config()
        
    def construct_shell_input(self, config_file_location: str = CONFIG_FILE) -> str:
        self.config_file = config_file_location 
        self.get_config()
        shell_status = []
        for status in self.core.modifier:
            shell_status.append(f"{status.color}|{status.display_name}|{Fore.RESET}")
        current_path = f"{Fore.CYAN}{' ~' if os.getcwd() == str(self.core.homedir) else ' ' + os.getcwd()}{Fore.RESET}"
        shell_icon = "# " if self.core.root_access else "$ " 
        shell_input: list[str] = self.config.split("|")
        for idx, item in enumerate(shell_input):
            match item:
                case s if "shellstatus" in s:
                    item = "".join(shell_status)

                case s if "path" in s:
                    item = current_path

                case s if "shellicon" in s:
                    item = shell_icon
            shell_input[idx] = item


        return "".join(shell_input)


