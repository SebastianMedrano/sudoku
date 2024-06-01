class Board():
    def __init__(self,initial_state: list ) -> None:
        if not self._is_valid_state(initial_state):
            raise ValueError("Invalid initial state")
        square = len(initial_state)**0.5
        if square**2 != len(initial_state):
            raise ValueError("Invalid lenght of rows and columns")
        self._state = initial_state
        self._sub_grid_size = int(square)
        self._size = len(initial_state)

    def get_state(self) -> bool:
        return self._state

    def set_value(self, row: int, col: int, value: int) -> bool:
        if not self._is_valid_move(row, col, value):
            return False
        self._state[row][col] = value
        return True
    def is_complete(self) -> bool:
        return all(all(cell != 0 for cell in row) for row in self._state)

    def is_valid(self) -> bool:
        return (self._are_rows_valid() and
                self._are_columns_valid() and
                self._are_subgrids_valid())

    def _is_valid_state(self, state: list) -> bool:
        row_len = len(state)
        return isinstance(state, list) and all(len(row) == row_len for row in state)

    def _is_valid_move(self, row: int, col: int, value: int) -> bool:
        if self._state[row][col] != 0:
            return False
        self._state[row][col] = value
        is_valid = self.is_valid()
        self._state[row][col] = 0
        return is_valid

    def _are_rows_valid(self) -> bool:
        for row in self._state:
            if not self._is_unique(row):
                return False
        return True

    def _are_columns_valid(self) -> bool:
        for col in zip(*self._state):
            if not self._is_unique(col):
                return False
        return True

    def _are_subgrids_valid(self) -> bool:
        for i in range(0, self._size, self._sub_grid_size):
            for j in range(0, self._size, self._sub_grid_size):
                subgrid = [self._state[x][y] for x in range(i, i + self._sub_grid_size) for y in range(j, j + self._sub_grid_size)]
                if not self._is_unique(subgrid):
                    return False
        return True

    def _is_unique(self, group) -> bool:
        elements = [x for x in group if x != 0]
        return len(elements) == len(set(elements))
    
    def __str__(self):
        sudoku = "\n"
        sudoku += "\n".join([" ".join(map(str, i)) for i in self._state])
        sudoku+="\n"
        return sudoku


        