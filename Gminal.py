import sys

print("Preparing load")
import os
dirchck = os.listdir()
if "test_g_project" in dirchck:
    from colorama import *
    print(Fore.RED + "ERROR")
    print("Git test cannot be run")
    print(" ")
    print(Fore.CYAN + "0003")
    print("")
    print(Fore.RESET + "Press enter to exit")
    input("")
    quit(1)
print("Testing git")

import os
from subprocess import check_output
try:
    cmd = 'git clone https://github.com/ItzFimes/test_g_project'
    check_output(cmd, shell=True).decode()
except:
    import os
    os.system("winget install --id Git.Git -e --source winget")
    print("Gminal needs to be restarted to apply changes")
    input("Press enter to exit")
    quit()


def storage_setup():
    print("Setting up current directory")
    setupfile = open(".gminal", "w+")
    setupfile.write(os.getcwd() + "\n" + "Gminal.setup.manual\n" + "1%\n" + "wait()\n" + "100%\n" + "Done\n")


def typingPrint(text, timer):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(timer)


def turtleislandgenerator():
    import turtle
    import math
    import random
    import time
    turtle.setup(1000, 1000)
    turtle.title("Random Island Generator")
    turtle.speed(0)
    turtle.hideturtle()

    def draw_line(x1, y1, x2, y2):
        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)

    def dist(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def shoreline(x1, y1, x2, y2, ratio):
        L = dist((x1, y1), (x2, y2))
        if L <= 1:
            draw_line(x1, y1, x2, y2)
            return
        rs = ratio + random.uniform(-0.1, 0.1)
        rs = max(0.5, rs)
        midx = (x1 + x2) / 2
        midy = (y1 + y2) / 2
        rx = L / 2 + (2 * rs - 1) / 2 * L
        ry = ((L * rs) ** 2 - (L / 2) ** 2) ** 0.5
        theta = math.atan2(y2 - y1, x2 - x1)
        alpha = random.uniform(math.pi * 0.3, math.pi * 0.7)
        x3 = rx * math.cos(alpha) * math.cos(theta) - ry * math.sin(alpha) * math.sin(theta) + midx
        y3 = rx * math.cos(alpha) * math.sin(theta) + ry * math.sin(alpha) * math.cos(theta) + midy
        shoreline(x1, y1, x3, y3, ratio)
        shoreline(x3, y3, x2, y2, ratio)

    turtle.tracer(0, 0)
    turtle.bgcolor('royal blue')
    turtle.pencolor('green')
    turtle.fillcolor('forest green')
    turtle.begin_fill()
    shoreline(-300, 0, 300, 0, 0.55)  # call recursion
    shoreline(300, 0, -300, 0, 0.55)  # call recursion
    turtle.end_fill()
    turtle.update()
    time.sleep(3)


def turtlehelixgenerator():
    # Python program to draw
    # Spiral Helix Pattern
    # using Turtle Programming

    import turtle
    loadWindow = turtle.Screen()
    turtle.speed(2)

    for i in range(100):
        turtle.circle(5 * i)
        turtle.circle(-5 * i)
        turtle.left(i)

    turtle.exitonclick()


print("Loading...")
import os
import shutil


print("Loading 1%")
import time

print("Loading 2%")
import tkinter

print("Loading 3%")
import colorama
from colorama import Fore, Back, Style

print("Loading 4%")
import subprocess, platform

print("Loading 5%")
from basic import login

print("Loading 6%")
import subprocess

o = 6
for i in range(94):
    o = o + 1
    o2 = str(o)
    time.sleep(0.01)
    print("Loading " + o2 + "%")
time.sleep(2)
if "TaH" in dirchck:
    print(Fore.LIGHTWHITE_EX + "(pulling files from TaH)")
    os.chdir("TaH")
    os.chdir("rickrolling")
    rckrllfileread = open("rickroll_link.txt", "r")
    rckrllfilereaded = rckrllfileread.read()
    rckrllfileread.close()
    os.chdir("totallyrealvegas")
    ttlyrealvgsread = open("cmd.py", "r")
    ttlyrealvgsreaded = ttlyrealvgsread.read()
    ttlyrealvgsread.close()
    print(Fore.RESET + "Copying bytes")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    print(Fore.GREEN + "Done!" + Fore.RESET)
    time.sleep(1)
    time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.GREEN + """

                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                           .°*oooo*°                                             
                                         °O#o*°°°**O°                                            
                                        O@*                                                      
                                       o@°                                                       
                                       ##      *ooo**                                            
                                       ##.     °°°*@O                                            
                                       °@O         #O                                            
                                        °O#o°.....*@O                                            
                                          .*oOOOOoo°.                                            
                                                                                                 
                                                                                                 
                     O#°       .O#.  °#.  °#O.     °#      °#O      °#                           
                     @o#°     .#o@.  °@.  *@*#*    *@     .@°OO     *@                           
                     #°°@.    #*.#.  °#.  °#  OO   *#     #*  #*    *#                           
                     @° *#.  #o °@.  °@.  °@.  o#° *@    O#...*@°   *@                           
                     #°  *#.#o  °#.  °#.  °#    °#*°#   *#*****o@.  *#                           
                     @°   *@o   °@.  °@.  *@.     O#@. °@°      o#  *@*°*°*                      
                     °     .     °    °    °       °°  °.        °.  °°°°°°                      
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
               ..°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°.°°°°°.               
             *##OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOooooOOoOOOoOooo#O°            
            *@*                                                          °*°** ..°°o@°           
            O#                                                     ****  Oo.*# o##..#*           
            O@.                                         ...........    ...***..*.°°*@*           
            O@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#@*           
            O@.                                                                    °@*           
            O@.                                                                    °@*           
            O@.                                                                    °@*           
            O@.                                                                    °@*           
            O@.                                                                    °@*           
            O@.                                                                    °@*           
            O@.                      o*°.                                          °@*           
            O@.                       .°***°                                       °@*           
            O@.                         °*Oo.                                      °@*           
            O@.                      *o*°.                                         °@*           
            O@.                      .                                             °@*           
            O@.                                °°°°°°°°                            °@*           
            O@.                                ........                            °@*           
            O#.                                                                    °#*           
            O@.                                                                    *@*           
            .O#o°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°*o#o            
              .*oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo*.             
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 



""")
try:
    import subprocess
    import shutil
    import os
    import stat
    from os import path

    for root, dirs, files in os.walk("test_g_project"):
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    shutil.rmtree('test_g_project')
except OSError as error:
    print(error)
    print("--------------")
terminalico = ">"
while True:
    try:
        print(Style.RESET_ALL)
        cmdc = input(terminalico)
        cmdnds = ["help", "terminal icon", "clear", "dir", "cd"]
        if cmdc == "help":
            print(Fore.YELLOW + "-------- HELP --------")
            print("")
            print(Fore.YELLOW + "---------- BASIC HELP ----------")
            print(Fore.GREEN + "tkinter |Shows things using python tkinter interface(not done yet)| ")
            print(Fore.GREEN + "clear   |Clears the terminal|")
            print(Fore.GREEN + "dir     |Shows current directory and items in it|")
            print(Fore.GREEN + "terminal icon |Changes the chracter on the beginning of command line|")
            print(Fore.GREEN + "cd      |Changes directory|")
            print(Fore.GREEN + "read    |Reads content of file|")
            print(Fore.GREEN + "exit    |Exits the app|")
            print(Fore.GREEN + "openexe |Opens .exe file|")
            print(Fore.GREEN + "windowscmd |Executes command using windows terminal (windows only)|")
            print(Fore.YELLOW + "---------- BASIC HELP ----------")
            print("")
            print(Fore.YELLOW + "-------- TKINTER MODULE --------" + Fore.RESET)
            print(Fore.GREEN + "tk -turtle --<parameter> |For available parameters type tk -help, Runs tkinter turtle program|")
            print(Fore.GREEN + "tk -old --<parameter> |For available parameters type tk -help, Runs my old project(might not be tkinter project)|")
            print(Fore.YELLOW + "-------- TKINTER MODULE --------" + Fore.RESET)
            print(Fore.YELLOW + "-------- HELP --------")

#basic
        if cmdc == "terminal icon":
            print(Fore.RED + "Please enter symbols that you want your terminal prompt icon to be" + Fore.RESET)
            terminalico = input("")
        if cmdc == "clear":
            print("Clearing in 3 seconds")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        if cmdc == "dir":
            print(Fore.GREEN + os.getcwd())
            print(Fore.RESET)
            print("")
            print(os.listdir())
        if cmdc == "cd":
            try:
                newdir = input(Fore.LIGHTGREEN_EX + "Directory: " + Fore.RESET)
                os.chdir(newdir)
            except:
                print(Fore.RED + "Invalid directory" + Fore.RESET)
        if cmdc == "read":
            readfile = input(Fore.GREEN + "File name: ")
            filetoread = open(readfile, "r")
            filereaded = filetoread.read()
            filetoread.close()
            print(filereaded)
        if cmdc == "exit":
            print(Style.RESET_ALL)
            sys.exit(1)
        if cmdc == "openexe":
            exetoopen = input("Name of the exe file: ")
            subprocess.call([exetoopen])
        if cmdc == "windowscmd":
            exetostart = input("Please enter command : ")
            os.system(exetostart)
        if cmdc == "support":
            print(Fore.YELLOW + "----- SUPPORT US -----" + Fore.RESET)
            print(Fore.LIGHTMAGENTA_EX + "Instagram" + Fore.RESET)
            print("     @itz_fimes")
            print("     @fimes_does_dev_stuff")
            print("     @operating.system.g")
        if cmdc == "del":
            try:
                delfile = input(Fore.YELLOW + "File name: ")
                delfilesure = input(Fore.RESET + Fore.RED + "Are you sure you want to delete this file? [Y/N] ")
                if delfilesure == "Y":
                    print(Fore.RED + "Deleting file..." + Fore.RESET)
                    os.remove(delfile)
                else:
                    print("Deleting canceled.")
                    print(Fore.YELLOW + "Print if you answered y/yes/yeah please answer Y" + Fore.RESET)
            except:
                print(Fore.RED + "File does not exist")
        if cmdc == "storage-setup":
            print("Setting up....")
            storage_setup()
        if cmdc == "I vented":
            print(Fore.RED + "You what?!" + Fore.RESET)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
            
                
            
            
            """)
            typingPrint("User was the impostor....", 0.1)
            print("""










                        """)
            terminalico = "ඞ> "

        if cmdc == "deldir":
            try:
                deldir = input(Fore.YELLOW + "Directory: ")
                deldirsure = input(Fore.RESET + Fore.RED + "Are you sure you want to delete this directory? [Y/N] ")
                if deldirsure == "Y":
                    print(Fore.RED + "Deleting directory..." + Fore.RESET)
                    shutil.rmtree(deldir)
                else:
                    print("Deleting canceled.")
                    print(Fore.YELLOW + "Print if you answered y/yes/yeah please answer Y" + Fore.RESET)
            except OSError as error:
                print(error)
                print("Directory '% s' can not be removed" % deldir)

        #TaH
        if cmdc == "setup tah":
            print("Preparing")
            print("Preparing git")

            installdir = os.listdir()
            print(installdir)
            if "TaH" in installdir:
                print(Fore.RED + "Can't install TaH because TaH already exist" + Fore.RESET)
                time.sleep(1)
                continue
            if "storage" in installdir:
                print("Verifying directory 1/3")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "basic" in installdir:
                print("Verifying directory 2/3")
            else:

                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "Gminal.py" in installdir:
                print("Installing(Verified 3/3)")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            from subprocess import check_output

            cmd = 'git clone https://github.com/ItzFimes/TaH'
            check_output(cmd, shell=True).decode()
            time.sleep(2)
            print(Fore.GREEN + "Updating dirchck..." + Fore.RESET)

        if cmdc == "update tah":

            print("Preparing")
            print("Preparing git")

            updtdir = os.listdir()
            print(updtdir)
            if "storage" in updtdir:
                print("Verifying directory 1/3")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "basic" in updtdir:
                print("Verifying directory 2/3")
            else:

                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "Gminal.py" in updtdir:
                print("Installing(Verified 3/3)")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            print("Deleting old TaH...")
            try:
                import subprocess
                import shutil
                import os
                import stat
                from os import path

                for root, dirs, files in os.walk("TaH"):
                    for dir in dirs:
                        os.chmod(path.join(root, dir), stat.S_IRWXU)
                    for file in files:
                        os.chmod(path.join(root, file), stat.S_IRWXU)
                shutil.rmtree('TaH')
            except OSError as error:
                print(error)
                print("--------------")
                continue
            print("Installing new TaH...")
            from subprocess import check_output

            cmd = 'git clone https://github.com/ItzFimes/TaH'
            check_output(cmd, shell=True).decode()
            time.sleep(2)
            print(Fore.GREEN + "Updating dirchck..." + Fore.RESET)
            dirchck = os.listdir()

        if "TaH" in dirchck:

            if cmdc == "tah -rckrl --links":
                print(Fore.BLUE + "Thanks to:")
                print(Fore.CYAN + "   discordgift.site")
                print(Fore.CYAN + "   brojsimpson.com/pranks/hidden-rick-roll-video-link-collection-rickrolled/")
                time.sleep(2)
                print(Fore.RESET + "")
                print(rckrllfilereaded)

            if cmdc == "tah -rckrl --ttlrlvgs":
                print(Fore.YELLOW + "(WORK_INFO) " + Fore.BLUE + "Setting up ttlrlvgs.py")
                ttlrlvgscreate = open("ttlrlvgs.py","w+")
                ttlrlvgscreate.write(ttlyrealvgsreaded)
                ttlrlvgscreate.close()
                print(Fore.GREEN + "Done")


                print(Fore.RESET + "Nice")
                print("I hope you aren't lying")
                print("Doin' da .exe convert thingy")
                shbatttlrlvgscrt = open("setup.bat","w+")
                shbatttlrlvgscrt.write('pyinstaller --noconfirm --onefile --windowed --debug "all" --hidden-import "keyboard" --hidden-import "mouse"  "ttlrlvgs.py"')
                shbatttlrlvgscrt.close()
                print()
                print(Fore.BLUE + "Setup done!")
                time.sleep(2)
                print("To setup ttlrlvgs.py open setup.bat")
                time.sleep(2)
                print(Fore.GREEN + "Your rickroll will be in:" + Fore.CYAN + " current dir\dist ")


        #tk

        if cmdc == "setup tk":
            print("Preparing")
            print("Preparing git")

            installdir = os.listdir()
            print(installdir)
            if "tk" in installdir:
                print(Fore.RED + "Can't install tk because tk already exist" + Fore.RESET)
                time.sleep(1)
                continue
            if "storage" in installdir:
                print("Verifying directory 1/3")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "basic" in installdir:
                print("Verifying directory 2/3")
            else:

                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "Gminal.py" in installdir:
                print("Installing(Verified 3/3)")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            from subprocess import check_output

            cmd = 'git clone https://github.com/ItzFimes/tk'
            check_output(cmd, shell=True).decode()
            time.sleep(2)
            print(Fore.GREEN + "Updating dirchck..." + Fore.RESET)
            dirchck = os.listdir()
        if cmdc == "update tk":

            print("Preparing")
            print("Preparing git")

            updtdir = os.listdir()
            print(updtdir)
            if "storage" in updtdir:
                print("Verifying directory 1/3")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "basic" in updtdir:
                print("Verifying directory 2/3")
            else:

                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "Gminal.py" in updtdir:
                print("Installing(Verified 3/3)")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            print("Deleting old tk...")
            try:
                import subprocess
                import shutil
                import os
                import stat
                from os import path

                for root, dirs, files in os.walk("tk"):
                    for dir in dirs:
                        os.chmod(path.join(root, dir), stat.S_IRWXU)
                    for file in files:
                        os.chmod(path.join(root, file), stat.S_IRWXU)
                shutil.rmtree('tk')
            except OSError as error:
                print(error)
                print("--------------")
            print("Installing new tk...")
            from subprocess import check_output

            cmd = 'git clone https://github.com/ItzFimes/tk'
            check_output(cmd, shell=True).decode()
            time.sleep(2)
            print(Fore.GREEN + "Updating dirchck..." + Fore.RESET)
            dirchck = os.listdir()

        if cmdc == "del tk":
            print(Fore.RED + "Deleting tk" + Fore.RESET)
            time.sleep(3)
            print("Preparing")
            print("Preparing git")

            deldir= os.listdir()
            if "tk" not in deldir:
                print(Fore.RED + "Path " + Fore.GREEN + r"~\tk " + Fore.RED + "doesn't exist" + Fore.RESET)
                time.sleep(1)
                continue
            print(deldir)
            if "storage" in deldir:
                print("Verifying directory 1/3")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "basic" in deldir:
                print("Verifying directory 2/3")
            else:

                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            if "Gminal.py" in deldir:
                print("Deleting(Verified 3/3)")
            else:
                print(Fore.RED + "You must be in directory that Gminal.exe is installed in" + Fore.RESET)
                continue
            print("Deleting tk...")
            try:
                import subprocess
                import shutil
                import os
                import stat
                from os import path

                for root, dirs, files in os.walk("tk"):
                    for dir in dirs:
                        os.chmod(path.join(root, dir), stat.S_IRWXU)
                    for file in files:
                        os.chmod(path.join(root, file), stat.S_IRWXU)
                shutil.rmtree('tk')
                time.sleep(2)
                print(Fore.GREEN + "Updating dirchck..." + Fore.RESET)
                dirchck = os.listdir()
            except OSError as error:
                print(error)
                print("--------------")

        if cmdc == "tk -help":
                print(Fore.YELLOW + "-------- TKINTER HELP --------" + Fore.RESET)
                print("")
                print(Fore.YELLOW + "---------- BASIC TK COMMANDS ----------")
                print(Fore.GREEN + "tk -help|Shows this menu|")
                print(Fore.GREEN + "tk -update|Updates tk|")
                print(Fore.GREEN + "del tk|Deletes tk|")
                print(Fore.YELLOW + "---------- BASIC TK COMMANDS ----------")
                print("")
                print(Fore.YELLOW + "-------- TK -OLD --------")
                print(Fore.BLUE + "Tk old is used to view my old projects|")
                print(Fore.GREEN + "tk -old --windos|Shows my old project named windos|")
                print(Fore.GREEN + "tk -old --WinOfMilk|Shows my first game made in python named Window of milk|")
                print(Fore.GREEN + "tk -old --Gos|Opens really old version of Operating system G|")
                print(Fore.YELLOW + "-------- TK -OLD --------")
                print("")
                print(Fore.YELLOW + "---------- TK -TURTLE ----------")
                print(Fore.GREEN + "tk -turtle --island|Generates random island|")
                print(Fore.YELLOW + "---------- TK -TURTLE ----------")
                print("")
                print(Fore.YELLOW + "---------- TKINTER HELP ----------")
        try:
            if "tk" in dirchck:

                if cmdc == "tk -old --Gos":
                    print(Fore.RED + "You must be in the root directory" + Fore.GREEN + "(directory that you installed Gminal in)" + Fore.RESET)
                    subprocess.call([r"tk\G_os\OS.exe"])

                if cmdc == "tk -old --WinOfMilk":
                    print(
                        Fore.RED + "You must be in the root directory" + Fore.GREEN + "(directory that you installed Gminal in)" + Fore.RESET)
                    print("Fun fact: This was my first game i programmed in python")
                    print(Fore.BLUE + "This game will probably work in/with gminal")
                    print(Fore.RED + "")
                    time.sleep(5)
                    subprocess.call(["tk\WinOfMilk\Game.exe"])

                if cmdc == "tk -turtle --island":
                    print("Thanks to PythonTurtle.Academy for this code!")
                    turtleislandgenerator()
                if cmdc == "tk -old --windos":
                    print(
                        Fore.RED + "You must be in the root directory" + Fore.GREEN + "(directory that you installed Gminal in)" + Fore.RESET)
                    print("Fun fact: This was Gminal before it eas renamed to Gminal")
                    print(Fore.BLUE + "To exit windos type" + Fore.GREEN + "Ghoose --honk" + Fore.RESET)
                    print(Fore.RED + "")
                    time.sleep(5)
                    subprocess.call(["tk\Windos\Windos.exe"])
        except:
            print(Fore.RED + "Module tk isn't feeling like doing that right now.")
            print(Fore.BLUE + "(that means some error occurred)")
            print(Fore.RESET + "")
            print(Fore.CYAN + "Restarting Gminal should fix it")
            print("If restarting doesn't fix it contact me on ig: " + Fore.MAGENTA + "@fimes_does_dev_stuff")
            continue
    #Fallback

    except:
        print(Fore.RESET)
        print(Back.RED + "Fatal error" + Back.RESET)
        c = input(Fore.RED + "Do you want to exit[Y/N]" + Fore.RESET)
        if c == "Y":
            quit()
        if c == "y":
            print(Fore.RED + "Did you mean" + Fore.RESET + Fore.GREEN + " Y" + Fore.RESET)
            print("Probably yes")
            time.sleep(2)
            quit()
        if c == "Yes":
            print(Fore.RED + "Did you mean" + Fore.RESET + Fore.GREEN + " Y" + Fore.RESET)
            print("Probably yes")
            time.sleep(2)
            quit()
        if c == "yes":
            print(Fore.RED + "Did you mean" + Fore.RESET + Fore.GREEN + " Y" + Fore.RESET)
            print("Probably yes")
            time.sleep(2)
            quit()
        else:
            print("We will try to recover your terminal")
            time.sleep(1)
            print(
                Fore.CYAN + "Developers note:" + Fore.RED + "I have no idea if it will work or not. Its almost 50/50 chance" + Fore.RESET)
            time.sleep(1)
            print("Here comes the magic")
            time.sleep(3)
            print("Recovered!(Hopefully)")
