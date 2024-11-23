from utils import package_manager
from utils.print_utils import print
from core.core import CoreFunctionality
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
    "%p's finally gone :>",
    "plinK"
]

install_text = [
    "Target %p has been successfuwwy depwoyed! >:3...",
    "Instawwation compwete! We wewcome %p to the pawty :3...",
    "%p has been added to youw awmy of awesome too~s :>",
    "Good news! %p is now comfy in youw system uwu...",
    "%p is aww set up and weady to wowk its magic :3...",
    "Mission accompwished, %p is weady to wock and woww >:3...",
    "Confiwmation compwete, %p has joined youw side :3...",
    "Instawwation successfuwwy pewfowmed! %p is now youws uwu...",
    "%p is in da house, west assured it's pwugged in :3...",
    "Task compweted... %p is officiawwy one of youws >:3...",
    "%p insta~~wation done... genius stwikes again >:3...",
    "Done and dusted! %p's weady to go uwu...",
    "Weww weww weww, %p is up and wunning uwu...",
    "Aww done! %p is now good to go uwu :3...",
    "Instawwation compwete! Pewfect execution as awways uwu >:3...",
    "Success! %p is wocking its pwace uwu...",
    "Say hewwo to youw new fwend, %p uwu >:3...",
    "Done!",
    "Finished!",
    "Nothing to do.",
    "What a piece of cake 'twas",
    "Welcome %p to the family."
    "Elloo %p",
    "%p is officially here, say hello :3",
    "Success!",
    "helloo~~ %p <3",
    "insert install finished message here",
    "%p is plinKing here",
    "%p is a champion sonny.",
    f"{Fore.BLUE}@%p{Fore.GREEN} GET INSTALLED LOL",
    "is %p just gonna be another package in the package list? Or will you do something with it?",
    "%p is gonna change the world one day! :3",
    "Bingo Bango Bongo, Bish Bash Bosh",
    f"{Fore.BLUE}@everyone @%p{Fore.GREEN} is here!"
]


def execute(self, *args):
    """gpm is a command wrapper for Gminal's package manager"""
    gpm = package_manager.GminalPackageManager(
        packagelist_path=f"{self.startingdir}/utils/package_manager/packagelist.gres",
        core=self,
        installlistpath=f"{self.startingdir}/utils/package_manager/installed_packages.gres")  # Init the package manager
    command = args
    try:
        package_name = command[1]
    except IndexError:
        package_name = None
    try:
        instruction = command[0]
    except IndexError:
        instruction = None
    if instruction == "install" or instruction == "-i":
        try:
            gpm.install_package(package_name)  # Pass package name and install package
            print(Fore.GREEN + install_text[random.randint(0, len(install_text))].replace("%p",
                                                                                          package_name))  # Yipeeee if it installs
        except Exception as e:
            print(f"Failed to install package '{package_name}' :c, because: {Fore.RED}{e}")  # cry if it doesn't :c
    elif instruction == "uninstall" or instruction == "-u":
        try:
            gpm.uninstall_package(package_name)
            print(Fore.GREEN + uninstall_text[random.randint(0, len(uninstall_text))].replace("%p", package_name))
        except Exception as e:
            print(f"Failed to uninstall package '{package_name}' :c, because: {Fore.RED}{e}")
    elif instruction == "list" or instruction == "-l":
        if package_name is not None:  # Check if more instructions were provided
            # To avoid confusion I use command[1] instead of package_name, bc package_name seems a bit misleading
            if command[1] == "available" or command[1] == "-a":
                list_p_type = "available"
            else:
                list_p_type = "installed"
            gpm.list_packages(list_p_type)
        else:  # If no more instructions were provided list the installed packages
            gpm.list_packages()

    else:
        raise Exception(f'Unknown instruction: {Fore.RED}"{instruction}"')

#
# execute(CoreFunctionality())
