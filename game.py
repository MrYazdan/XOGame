from module import *
from exceptions import *
from player import Player as _Player
from table import XOTable as _XOTable


class XOGame(_XOTable):

    def __init__(self, player1: _Player, player2: _Player) -> None:
        self.player1 = player1
        self.player2 = player2

        self.round = None
        self._winner = None

        # true value lists for calculate winner
        # [1, 2, 3] - [4, 5, 6] - [7, 8, 9]
        self.white_list = [[i, i + 1, i + 2] for i in range(1, 10, 3)]

        # [1, 4, 7] - [2, 5, 8] - [3, 6, 9]
        self.white_list.extend([[i, i + 3, i + 6] for i in range(1, 4)])

        # [3, 5, 7] - [1, 5, 9]
        self.white_list.extend([[5 - i, 5, 5 + i] for i in range(2, 5, 2)])

        print(self.white_list)

    def _calculate_result(self, cell_no):
        self.result = False
        white_list = self.white_list
        _map = super().xo_map

        for li in white_list:
            if all(list(map(lambda x: _map[x] == _map[cell_no], li))):
                self._winner = _map[cell_no]

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o']]):

        # if finished game ? if 'True'-> assert error
        assert not self._winner, FinishedGameError

        # set true value for sign
        player_sign = player.sign if isinstance(player, _Player) else player

        if self.round is None:
            # first round
            self.round = player_sign

        elif self.round == player_sign:
            # duplicate round
            raise RoundError()

        else:
            # round OK ! :)
            self.round = player_sign

        # save to _XOTable
        super().mark(cell_no, player_sign)

        # calculate result
        self._calculate_result(cell_no)

    @property
    def winner(self) -> _Player:

        # if not finished game ? if 'True'-> assert error
        assert self._winner, UnFinishedGameError

        # select winner player with sign
        winner_player = self.player1 if self.player1.sign == self._winner else self.player2

        return winner_player
