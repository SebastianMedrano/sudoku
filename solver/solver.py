from board import Board
from abc import ABC, abstractmethod


class Solver(ABC):
    def __init__(self, board):
        self.board = board

    @abstractmethod
    def solve(self):
        pass