from exceptions import *
from functions import *
from settings import Setting
from player import Player as _Player
from game import XOGame as _XOGame


# winner = game.winner
# print(winner.name, winner.sign)


def play():
    # Config :
    pl1 = _Player(Setting.PL1_NAME, "x")
    pl2 = _Player(Setting.PL2_NAME, "o")
    game = _XOGame(pl1, pl2)

    _name = pl1.name
    fulled_cell = 0
    turn = pl1.sign
    round_count = Setting.ROUND_COUNT

    while round_count != 0:
        while fulled_cell <= 9:
            welcome_page()
            termcolor.cprint(f"{'=' * 14} PLAY --> ROUND : {round_count} -> MARK {'=' * 14}", color="cyan")

            termcolor.cprint(game, color="cyan")
            print()

            _tmp = input(f" {_name.title()} Enter Number To Mark The Cell : ")
            _tmp = normalize_cell_no(_tmp)

            if _tmp == 0:
                welcome_page()
                termcolor.cprint(f"{'=' * 14} PLAY -> ROUND : {round_count} -> ERROR {'=' * 14}", color="cyan")
                print(" Please Enter True Value !\n Cell Is [1 ~ 9]\n")
                _tmp = input(" Press Enter To Try Again ~ ")
                continue

            try:
                game.mark(_tmp, turn)
            except:
                welcome_page()
                termcolor.cprint(f"{'=' * 14} PLAY -> ROUND : {round_count} -> ERROR {'=' * 14}", color="cyan")
                print(" Please Enter True Value !\n Cell Is [1 ~ 9] And Not Used !\n")
                _tmp = input(" Press Enter To Try Again ~ ")
                continue

            winner = game.winner
            if winner is not None:
                welcome_page()
                termcolor.cprint(f"{'=' * 14} PLAY --> ROUND : {round_count} -> WIN! {'=' * 14}", color="cyan")
                termcolor.cprint(game, color="cyan")
                print()
                termcolor.cprint(f"{winner.name} Is Winner in Round {round_count}", color="green")
                print()

                if winner.name == Setting.PL1_NAME:
                    Setting.PL1_WIN += 1
                else:
                    Setting.PL2_WIN += 1

            if fulled_cell == 9:
                welcome_page()
                termcolor.cprint(f"{'=' * 14} PLAY -> ROUND : {round_count} -> EQUAL {'=' * 14}", color="cyan")
                termcolor.cprint(game, color="cyan")
                print()
                termcolor.cprint(f"Players Is Equal in Round {round_count}", color="green")
                print()

            turn = "o" if turn == "x" else "x"
            _name = pl1.name if _name == pl2.name else pl2.name
            fulled_cell += 1
        round_count -=1

    welcome_page()
    termcolor.cprint(f"{'=' * 21} SHOW  RESULT {'=' * 21}", color="cyan")

    if Setting.PL1_WIN > Setting.PL2_WIN:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl1.name} Winner !", font="small"), color="blue")
        _res = f" {pl1.name} Winner !"
    elif Setting.PL1_WIN < Setting.PL2_WIN:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl2.name} Winner !", font="small"), color="blue")
        _res = f" {pl2.name} Winner !"
    else:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl1.name} EQUAL {pl2.name}", font="small"), color="yellow")
        _res = f" {pl1.name} EQUAL {pl2.name}"

    Setting.LAST_RESULT = _res
    print()
    _tmp = input(" Press Enter To Back Main ~ ")

    main()


def main() -> None:
    while True:

        welcome_page()
        termcolor.cprint(f"{'=' * 25} MAIN {'=' * 25}", color="cyan")

        print(
            """                    1. Start New Game        
                    2. Setting
                    3. Show Last Result

                    9. Report Bug
                    0. Exit The Game"""
        )

        termcolor.cprint("=" * 56, color="cyan")

        try:
            cmd = input(" Please enter number of command > ".title())
            assert iscommand("main", cmd), CommandError()

            if cmd == "0":
                exit_page("main")
                continue

            elif cmd == "1":
                start_game_panel()
                play()
                continue

            elif cmd == "2":
                setting_panel("main")
                continue

            elif cmd == "3":
                show_last_result()
                continue

        except AssertionError:
            command_error("main")
            continue


# main page starter  :)
if __name__ == '__main__':
    main()
