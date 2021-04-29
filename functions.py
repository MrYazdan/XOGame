from module import *
from settings import Setting


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
        termcolor.cprint(f"{'=' * 20} COMMAND  ERROR {'=' * 20}", color="cyan")
        print(" Print Your Command Was Not Defined! :(")
        _tmp = input(" Press Enter To Load Main Again ~")


def exit_page(_from: str) -> None:
    if _from == "main":
        welcome_page()
        termcolor.cprint(f"{'=' * 25} EXIT {'=' * 25}", color="cyan")
        print(" What Are You Doing !?")
        _tmp = input(" Are you sure to exit the game ? ".title() + "[y/N] : ")

        if _tmp.lower() == "y":
            welcome_page()
            termcolor.cprint(pyfiglet.figlet_format(" Goodbye !", font="small"), color="red")
            exit()


def setting_panel(_from: str) -> None:
    if _from == "main":
        welcome_page()
        termcolor.cprint(f"{'=' * 23} SETTINGS {'=' * 23}", color="cyan")

        print(
            f"""                    1. Round Count : {Setting.ROUND_COUNT}        
                    x. Coming Soon ...
                    
                    0. Back To Main"""
        )

        termcolor.cprint("=" * 56, color="cyan")
        cmd = input(" Please enter number of command > ".title())

        if cmd == "1":
            while True:
                welcome_page()
                termcolor.cprint(f"{'=' * 14} SETTING -> SET ROUND COUNT {'=' * 14}", color="cyan")
                _tmp = input(" Enter Number Of Round To Play Game [1 / 9] : ")

                if 1 <= int(_tmp) <= 9:
                    Setting.ROUND_COUNT = int(_tmp)
                    welcome_page()
                    termcolor.cprint(f"{'=' * 14} SETTING -> SET ROUND COUNT {'=' * 14}", color="cyan")
                    _tmp = input(" New Round Count Saved !\n Press Enter To Back Main ~ ")
                    break

                else:
                    welcome_page()
                    termcolor.cprint(f"{'=' * 14} SETTING -> SET ROUND COUNT {'=' * 14}", color="cyan")
                    _tmp = input(" Please Enter True Value !\n Press Enter To Continue ~ ")
                    continue


def start_game_panel():
    _tmp = []

    for i in range(2):
        welcome_page()
        termcolor.cprint(f"{'=' * 19} INITIALIZE  GAME {'=' * 19}", color="cyan")
        _tmp.append(input(f" Please Enter Name Of Player {i + 1} : "))

    Setting.PL1_NAME = _tmp[0]
    Setting.PL2_NAME = _tmp[1]

    welcome_page()
    termcolor.cprint(f"{'=' * 19} INITIALIZE  GAME {'=' * 19}", color="cyan")
    print()
    termcolor.cprint(f" Player 1 => {Setting.PL1_NAME} With Sign : 'X'", color="red")
    termcolor.cprint(f" Player 2 => {Setting.PL2_NAME} With Sign : 'O'", color="blue")
    print()
    termcolor.cprint(f"{'=' * 56}", color="cyan")
    _tmp = input(" Press Enter To Play Game ~ ")


def normalize_cell_no(string: str) -> int:
    try:
        string = int(string)

        if 1 <= string <= 9:
            return string
    except:
        return 0


def show_last_result():
    welcome_page()
    termcolor.cprint(f"{'=' * 21} SHOW  RESULT {'=' * 21}", color="cyan")
    print()
    _tmp = input(" Press Enter To Back Main ~ ")
