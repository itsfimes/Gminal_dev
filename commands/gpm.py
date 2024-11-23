from utils import package_manager
from utils.print_utils import print
from colorama import Fore
import colorama
import random

colorama.init(autoreset=True)

uninstall_text = [
    "Target %p eliminated successfully! :3",
    "%p has been yeeted into the void :3...",
    "Mission accompwished, %p is no more >:3...",
    "Goodbye, %p! I hawdwy knew ye >:3...",
    "Look at that, %p is gone like magic! :>",
    "Youw PC is now %p-free and happy!",
    "Pewfect execution! %p unwoaded safewy :3...",
    "All done! %p has been pewmanentwy banished >:3...",
    "Say youw wast goodbye to %p :c... it's gone!",
    "%p uninstaww compwete... pwease caww me a genius >:3...",
    "We got 'em all. None left.",
    "%p is outta here! :>",
    "%p is gonna regret wakin' up this mornin'",
    "I guess we got that mess sorted out...",
    "Bingo Bango Bongo, Bish Bash Bosh",
    "%p's finally gone :>"
]


def execute(self, *args):
    """gpm is a command wrapper for Gminal's package manager"""
    gpm = package_manager.GminalPackageManager(
        packagelist_path=f"{self.startingdir}/utils/package_manager/packagelist.gres",
        core=self, installlistpath=f"{self.startingdir}/utils/package_manager/installed_packages.gres")  # Init the package manager
    command = args
    try:
        package_name = command[1]
    except IndexError:
        package_name = "No package provided"
    instruction = command[0]
    if instruction == "install" or instruction == "-i":
        try:
            gpm.install_package(package_name)  # Pass package name and install package
            print(f"{Fore.GREEN}Package '{package_name}' installed successfully :33")  # Yipeeee if it installs
        except Exception as e:
            print(f"Failed to install package '{package_name}' :c, because: {Fore.RED}{e}")  # cry if it doesn't :c
    elif instruction == "uninstall" or instruction == "-u":
        try:
            gpm.uninstall_package(package_name)
            print(Fore.GREEN + uninstall_text[random.randint(0, len(uninstall_text))].replace("%p", package_name))
        except Exception as e:
            print(f"Failed to uninstall package '{package_name}' :c, because: {Fore.RED}{e}")
    else:
        raise Exception(f'Unknown instruction: {Fore.RED}"{instruction}"')
