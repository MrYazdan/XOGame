from module import *


def clear():
    system("cls") if name == "nt" else system("clear")


def welcome_page():
    termcolor.cprint("-" * 55, color="cyan")
    termcolor.cprint(pyfiglet.figlet_format(" |= XO Game"), color="green", end=" ")
    print("Source : https://github.com/MrYazdan/XOGame_Maktab52")
    print(" Version : 1.0.0  -  Developer : Yazdan")
    termcolor.cprint("-" * 55, color="cyan")
