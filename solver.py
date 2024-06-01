from board import Board
from abc import ABC, abstractmethod


class Solver(ABC):

    @abstractmethod
    def solve(self):
        pass