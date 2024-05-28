from board import Board
from abc import ABC, abstractmethod


class Solver(ABC):

    @abstractmethod
    def implementation(self, board: Board):
        pass