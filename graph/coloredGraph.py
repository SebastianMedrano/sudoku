import numpy as np
from board import Board
from graph.graph import Graph

class ColoredGraph(Graph):
    def __init__(self, board: Board) -> None:
        self.board = board
        self.size = board._size
        self.subgrid_size = board._sub_grid_size
        super().__init__([], False)
        self.add_connections(self._create_initial_connections())
        self._color_initial_nodes()

    def _create_initial_connections(self) -> list:
        connections = []
        for row in range(self.size):
            for col in range(self.size):
                node = (row, col)
                connections.extend(self._add_common_edges(node))
                connections.extend(self.add_filled_edges(node))
        return connections

    def _add_common_edges(self, node1: tuple) -> list:
        connections = []
        row, col = node1
        for i in range(self.size):
            if i != col:
                node2 = (row,i)
                connections.append((node1,node2))
            if i != row:
                node2 = (i,col)
                connections.append((node1,node2))
        subgrid_row_start = (row // self.subgrid_size) * self.subgrid_size
        subgrid_col_start = (col // self.subgrid_size) * self.subgrid_size
        for i in range(subgrid_row_start, subgrid_row_start + self.subgrid_size):
            for j in range(subgrid_col_start, subgrid_col_start + self.subgrid_size):
                if (i, j) != node1:
                    node2 = (i,j)
                    connections.append((node1,node2))
        return connections
    
    def add_filled_edges(self,node: tuple)->list:
        connections = []
        equal_value_nodes= []
        connections = []
        for node_in_graph in self._graph:
            if self.get_value(node_in_graph) == self.get_value(node) != 0:
                equal_value_nodes.append(node)
        for index, first_node in enumerate(equal_value_nodes):
            for second_node in equal_value_nodes[index:]:
                for neighbor in self.get_neighbors(second_node):
                    if not self.is_connected(first_node, neighbor):
                        connections.append((first_node,neighbor))
        return connections
    
    def color_node(self, node):
        possible_values = set(range(1, self.size + 1))
        for neighbor in self.get_neighbors(node):
            if self.get_value(neighbor) in possible_values:
                possible_values.remove(self.get_value(neighbor))
        if len(possible_values) == 1 and self.board.set_value(*node,next(iter(possible_values))):
            self.set_value(node, possible_values.pop())
    
    def _color_initial_nodes(self):
       for row in range(self.size):
            for cell in range(self.size):
                self.set_value((row,cell), self.board.get_state()[row][cell])