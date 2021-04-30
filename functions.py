from module import *
from settings import Setting


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


def welcome_page(string: str, count_ward: int):
    clear()
    termcolor.cprint("=" * 56, color="cyan")
    termcolor.cprint(pyfiglet.figlet_format(" |= XO Game"), color="green", end=" ")
    print(" Source : https://github.com/MrYazdan/XOGame_Maktab52")
    print(" Version : 1.0.0  -  Developer : Yazdan\n")

    if not (string == "" and count_ward == 0):
        termcolor.cprint(f"{'=' * count_ward}{string}{'=' * count_ward}", color="cyan")


def iscommand(_from: str, cmd: str) -> bool:
    if _from == "main":
        if cmd in ["0", "1", "2", "3", "9"]:
            return True
    return False


def command_error(_from: str) -> None:
    if _from == "main":
        welcome_page(" COMMAND  ERROR ", 20)
        _tmp = input(" Print Your Command Was Not Defined! :(\n Press Enter To Load Main Again ~")


def exit_page(_from: str) -> None:
    if _from == "main":
        welcome_page(" EXIT ", 25)
        _tmp = input(" What Are You Doing !?\n Are you sure to exit the game ? ".title() + "[y/N] : ")

        if _tmp.lower() == "y":
            welcome_page("", 0)
            termcolor.cprint(pyfiglet.figlet_format(" Goodbye !", font="small"), color="red")
            exit()


def setting_panel(_from: str) -> None:
    if _from == "main":
        welcome_page(" SETTINGS ", 23)

        print(
            f"""                    1. Round Count : {Setting.ROUND_COUNT}        
                    x. Coming Soon ...
                    
                    0. Back To Main"""
        )

        termcolor.cprint("=" * 56, color="cyan")
        cmd = input(" Please enter number of command > ".title())

        if cmd == "1":
            while True:
                welcome_page(" SETTING -> SET ROUND COUNT ", 14)
                _tmp = input(" Enter Number Of Round To Play Game [1 / 9] : ")

                if 1 <= int(_tmp) <= 9:
                    Setting.ROUND_COUNT = int(_tmp)
                    welcome_page(" SETTING -> SET ROUND COUNT ", 14)
                    _tmp = input(" New Round Count Saved !\n Press Enter To Back Main ~ ")
                    break

                else:
                    welcome_page(" SETTING -> SET ROUND COUNT ", 14)
                    _tmp = input(" Please Enter True Value !\n Press Enter To Continue ~ ")
                    continue


def start_game_panel():
    tmp_list = []

    for i in range(2):
        welcome_page(" INITIALIZE  GAME ", 19)
        tmp_list.append(input(f" Please Enter Name Of Player {i + 1} : "))

    Setting.PL1_NAME = tmp_list[0]
    Setting.PL2_NAME = tmp_list[1]

    welcome_page(" INITIALIZE  GAME ", 19)
    termcolor.cprint(f"\n Player 1 => {Setting.PL1_NAME} With Sign : 'X'", color="red")
    termcolor.cprint(f" Player 2 => {Setting.PL2_NAME} With Sign : 'O'\n", color="blue")

    termcolor.cprint(f"{'=' * 56}", color="cyan")
    _tmp = input(" Press Enter To Play Game ~ ")


def normalize_cell_no(data: str) -> int:
    if data.isnumeric():
        if 0 < int(data) < 10:
            return int(data)

    welcome_page(" PLAY -> GET TRUE VALUES FOR MARK ", 15)

    _data = input("\n Enter True Value For Select The Mark [1 ~ 9] : ")
    return normalize_cell_no(_data)


def show_last_result():
    welcome_page(" SHOW  RESULT ", 21)

    termcolor.cprint(f"\n >> {Setting.LAST_RESULT} \n", color="cyan")
    _tmp = input(" Press Enter To Back Main ~ ")
