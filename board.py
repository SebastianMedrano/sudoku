import numpy as np
class Board():
    def __init__(self, n: int, initial_board: list ) -> None:
        self.n = n 
        self.board= np.array(initial_board)
            

    def check_solution(self, solved_board: list) -> bool:
        solved_np = np.array(solved_board)
        board_unit = self.board.copy()
        board_unit[board_unit>1]=1
        dot_matrix = solved_np*board_unit
        if (dot_matrix==self.board).all():
            return False
        for i in range(0,self.n**2):
            if self.check_if_duplicates(solved_np[i,:]):
                return False
            if self.check_if_duplicates(solved_np[:,i]):
                return False
        for i in range(0,self.n**2,self.n):
            for j in range(0,self.n**2,self.n):
                if self.check_if_duplicates(solved_np[i:i+self.n,j:j+self.n].flatten()):
                    return False
        return True

    def check_if_duplicates(self, seq: list)->bool:
        return len(seq) != len(set(seq))

        