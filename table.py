from exceptions import *


class XOTable:
    xo_map = {k: None for k in range(1, 10)}

    def __str__(self):
        _map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[_map[i] if _map[i] else "-" for i in _map])

    def mark(self, cell_no, sign: str):
        # check cell_no in range int (1, 9+1)
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, InvalidCellError("Enter a valid cell no [1, 9]")

        # check cell_no is empty
        assert not self.xo_map[cell_no], "Cell is filled"

        # if sign is upper -> lower :)
        sign = str(sign).lower()

        # check sign in "xo"
        assert sign in 'xo', 'Invalid sign' + sign

        # insert sign to _XOTable
        self.xo_map[cell_no] = sign
