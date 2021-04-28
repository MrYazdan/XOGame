from module import *


def clear():
    system("cls") if name == "nt" else system("clear")


def welcome_page():
    clear()
    termcolor.cprint("=" * 56, color="cyan")
    termcolor.cprint(pyfiglet.figlet_format(" |= XO Game"), color="green", end=" ")
    print("Source : https://github.com/MrYazdan/XOGame_Maktab52")
    print(" Version : 1.0.0  -  Developer : Yazdan\n")


def iscommand(_from: str, cmd: str) -> bool:
    if _from == "main":
        if cmd in ["0", "1", "2", "3", "9"]:
            return True
    return False


def command_error(_from: str) -> None:
    if _from == "main":
        welcome_page()
        termcolor.cprint(f"{'='*20} COMMAND  ERROR {'=' * 20}", color="cyan")
        print("Print Your Command Was Not Defined! :(")
        _tmp = input("Press Enter To Load Main Again ~")


def exit_page(_from: str) -> None:
    if _from == "main":
        welcome_page()
        termcolor.cprint(f"{'=' * 25} EXIT {'=' * 25}", color="cyan")
        print("What Are You Doing !?")
        _tmp = input("Are you sure to exit the game ? ".title()+"[y/N] : ")

        if _tmp.lower() == "y":
            welcome_page()
            termcolor.cprint(pyfiglet.figlet_format("Goodbye !", font="small"), color="red")
            exit()
