from player import Player
from table import XOTable


class XOGame(XOTable):

    def __init__(self, player1: Player, player2: Player) -> None:
        # set player instances
        self.player1 = player1
        self.player2 = player2

        # initialize round = turn of player
        self.round = None
        self._winner = None

        # true value lists for calculate winner
        # [1, 2, 3] - [4, 5, 6] - [7, 8, 9]
        self.white_list = [[i, i + 1, i + 2] for i in range(1, 9 + 1, 3)]

        # [1, 4, 7] - [2, 5, 8] - [3, 6, 9]
        self.white_list.extend([[i, i + 3, i + 6] for i in range(1, 3 + 1)])

        # [3, 5, 7] - [1, 5, 9]
        self.white_list.extend([[5 - i, 5, 5 + i] for i in range(2, 4 + 1, 2)])

    def _calculate_result(self, cell_no):
        white_list = self.white_list

        # import cells and values
        _map = super().xo_map

        # process for select winner
        for li in white_list:
            if all(list(map(lambda x: _map[x] == _map[cell_no], li))):
                self._winner = _map[cell_no]

    def mark(self, cell_no):

        if self.round is None:
            # first round
            self.round = self.player1.sign

        # save to XOTable
        super()._mark(cell_no, self.round)

        if self.round == self.player1.sign:
            # change turn game ! -> from x to o
            self.round = self.player2.sign

        elif self.round == self.player2.sign:
            # change turn game ! -> from o to x
            self.round = self.player1.sign

        # calculate result
        self._calculate_result(cell_no)

    @property
    def winner(self):

        if self._winner is None:
            return None

        # select winner player with sign
        winner_player = self.player1 if self.player1.sign == self._winner else self.player2

        return winner_player

    def reset(self):
        XOTable.xo_map = {k: None for k in range(1, 10)}
        self.round = None
        self._winner = None

    def show_xo_dict(self):
        return self.__class__.xo_map
