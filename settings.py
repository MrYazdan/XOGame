from player import Player


class Setting:
    ROUND_COUNT = 3

    # Player1:
    PL1_NAME = None
    PL1_WIN = 0

    # Player2:
    PL2_NAME = None
    PL2_WIN = 0

    # Last Result:
    LAST_RESULT = "Empty Result !"


class Config:
    pl1 = Player(Setting.PL1_NAME, "x")
    pl2 = Player(Setting.PL2_NAME, "o")
