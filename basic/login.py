


def logininit():

    from colorama import Fore
    import os
    print("Initing login")
    logindone = open(r"login\logindone.ini", "a+")
    registerdone = logindone.read()
    print(registerdone)
    if registerdone == "0":
        print(Fore.YELLOW + "Uh oh... It looks like you aren't registered")
        usrname=input("Username: ")
        password=input("Password: ")

    else:
        print(Fore.GREEN + "Please login:")
    input()
    return