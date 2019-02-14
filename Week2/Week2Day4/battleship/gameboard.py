BLANK = ' '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'


class OverlapException:
    pass


class GameBoard:
    def __init__(self, width=5, height=5):
        grid = []
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
        self.grid = grid

    def __getitem__(self, index):
        col_index, row_index = index
        return self.grid[row_index][col_index]

    def __setitem__(self, index, value):
        col_index, row_index = index
        self.grid[row_index][col_index] = value

    def count(self, symbol):
        _count = 0
        for row in self.grid:
            for col in row:
                if col == symbol:
                    _count += 1
        return _count
