from exceptions import *
from functions import *
from settings import Setting
from player import Player
from game import XOGame as XOGame


def play():
    # assign players :
    pl1 = Player(Setting.PL1_NAME, "x")
    pl2 = Player(Setting.PL2_NAME, "o")

    name = pl1.name
    round_count = 1

    # initialize game
    game = XOGame(pl1, pl2)

    while round_count <= Setting.ROUND_COUNT:

        # count of fulled cells
        fulled_cell = 0

        while fulled_cell <= 9:

            welcome_page(f" PLAY --> ROUND : {round_count} -> MARK ", 14)
            termcolor.cprint(game, color="cyan")
            print()

            table = game.show_xo_dict()
            ui = normalize_cell_no(input(f" {name.title()} Enter True Number To Mark The Cell [1 ~ 9] : "), table)

            # mark the game table
            game.mark(ui)

            # select game winner
            winner = game.winner

            # check ! if winner is player instance
            if isinstance(winner, Player):
                welcome_page(f" PLAY --> ROUND : {round_count} -> WIN! ", 14)
                print()
                termcolor.cprint(pyfiglet.figlet_format(winner.name.upper(), font="small"), color="green", end=" ")
                termcolor.cprint(f"Is Winner in Round {round_count}\n", color="green")
                _tmp = input(" Press Enter To Continue ~ ")

                if winner.name == Setting.PL1_NAME:
                    Setting.PL1_WIN += 1
                else:
                    Setting.PL2_WIN += 1
                break

            if fulled_cell == 9:
                welcome_page(f" PLAY -> ROUND : {round_count} -> EQUAL ", 14)
                termcolor.cprint(f"\n Players Is Equal in Round {round_count}\n ", color="green")
                break

            name = pl1.name if name == pl2.name else pl2.name
            fulled_cell += 1

        # reset game for new round !
        game.reset()

        # increase round count
        round_count += 1

    # show result game
    welcome_page(" SHOW  RESULT ", 21)

    # print winner player :

    if Setting.PL1_WIN > Setting.PL2_WIN:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl1.name.upper()} Winner !", font="small"), color="blue")
        _res = f" {pl1.name} Winner !\n"

    elif Setting.PL1_WIN < Setting.PL2_WIN:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl2.name.upper()} Winner !", font="small"), color="blue")
        _res = f" {pl2.name} Winner !\n"

    else:
        termcolor.cprint(pyfiglet.figlet_format(f" {pl1.name}  EQUAL  {pl2.name}", font="small"), color="yellow")
        _res = f" {pl1.name} EQUAL {pl2.name}\n"

    # save result to last result
    Setting.LAST_RESULT = _res
    print()
    _tmp = input(" Press Enter To Back Main ~ ")


def main() -> None:
    while True:

        welcome_page(" MAIN ", 25)

        print(
            """                    1. Start New Game        
                    2. Setting
                    3. Show Last Result

                    9. Report Bug ( coming soon! )
                    0. Exit The Game"""
        )

        termcolor.cprint("=" * 56, color="cyan")

        try:
            cmd = input(" Please enter number of command > ".title())
            assert iscommand("main", cmd), CommandError()

            if cmd == "0":
                exit_page("main")
                continue

            if cmd == "1":
                start_game_panel()
                play()
                continue

            if cmd == "2":
                setting_panel("main")
                continue

            if cmd == "3":
                show_last_result()
                continue

        except:
            command_error("main")
            continue


# main page starter  :)
if __name__ == '__main__':
    main()
