from solver.solver import Solver
from graph.coloredGraph import ColoredGraph
class ColoredGraphSolver(Solver):
    def __init__(self, board):
        super().__init__(board)
        self.colored_graph = ColoredGraph(board)
    
    def solve(self,):
        while(not self.colored_graph.board.is_complete()):
            print(str(self.colored_graph.board))
            for row in range(self.colored_graph.size):
                for cell in range(self.colored_graph.size):
                    if self.colored_graph.board.get_state()[row][cell]==0:
                        self.colored_graph.color_node((row,cell))
                    else:
                        self.colored_graph.add_connections(self.colored_graph.add_filled_edges((row,cell)))
        if self.colored_graph.board.is_valid():
            return self.colored_graph.board.get_state()
        else:
             raise Exception("Error")
    