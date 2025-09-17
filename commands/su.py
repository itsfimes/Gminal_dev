# Superuser shell manager
import os


def execute(core, *args):
    command = args
    try:
        arg = command[0]
    except IndexError:
        arg = "Nope :<"
    if core.root_access:
        print("Already running as root. Executing a new shell anyway.")
    if arg == "sys" or arg == "-s":
        os.system("su")
    else:
        os.system(f'sudo python {core.startingdir}/Gminal.py --before-load-dir "{core.startingdir}" --after-load-dir "{os.getcwd()}" --no-welcome --silent-startup --silent-exit')
        print()