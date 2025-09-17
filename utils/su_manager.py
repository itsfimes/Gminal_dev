# Superuser managment util for Gminal
from utils.print_utils import print
import subprocess

class SuperUserManager:
    def __init__(self, core):
        self.core = core
        print("Init superuser managment: [utils.su_manager.init]", condition=self.core.debug_mode)
    
    def sudo_exec(self, command):
        if isinstance(command, str):
            command = command.split(" ")
        command.insert(0, "sudo")

        print(command, type(command), condition=self.core.debug_mode)
        try:
            # Run the sudo command securely
            result = subprocess.run(
                command,
                check=False,  # Don't raise an exception immediately
                capture_output=True,  # Capture stdout and stderr
            )

            if result.returncode != 0:  # Non-zero return code indicates failure
                # Check if the error was due to permission denial
                if b"a password is" in result.stderr.lower():
                    raise PermissionError("Sudo prompt was cancelled or failed due to incorrect credentials.")
                else:
                    raise Exception(f"Failed to sudo for {command}: {result.stderr.decode().strip()}")

        except PermissionError as e:
            raise Exception(f"Error: {e}")

    def sudo_check(self):
        try:
            self.sudo_exec("echo ''")
            return True  # TODO: Might be better with finally statement, look into that
        except PermissionError:
            return False
        except KeyboardInterrupt:
            return False