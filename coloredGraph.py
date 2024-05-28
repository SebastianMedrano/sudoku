import numpy as np
from board import Board
from graph import Graph
from solver import Solver

class ColoredGraphSolution(Graph, Solver):
    
    def __init__(self, board: Board):
        connections = []
        for i in range(0, board.n**2):
            for j in range(0, board.n**2): 
                for k in range(j+1, board.n**2):
                    connections.append(("{}_{}".format(i,j),"{}_{}".format(i,k)))
                    connections.append(("{}_{}".format(j,i),"{}_{}".format(k,i)))
                    
        for i in range(0, board.n**2, board.n):
            for j in range(0, board.n**2,board.n):
                sub_group=[]
                for k in range(i, i+board.n):
                    for l in range(j, j+board.n):
                        sub_group.append("{}_{}".format(k,l))
                for z in range(0,len(sub_group)):
                    for m in range(z+1,len(sub_group)):
                        connections.append((sub_group[z],sub_group[m]))
                sub_group.clear()
             
        super().__init__(connections, False)
    def implementation(self, board: Board):
        solution = board
        count=0
        while((not board.check_solution(solution.board)) and count<10):
            print(count)
            print(str(solution.board))
            for i in range(0, board.n**2):
                for j in range(0, board.n**2):
                    if solution.board[i][j]==0:
                        solution.board[i][j]=self.get_value(i,j,solution)
                    else:
                        self.link_nodes_same_values((i,j), solution)
             
            count +=1
        return solution
    
    def link_nodes_same_values(self, position: tuple, solution: Board):
        equal_nodes= []
        filled_nodes = []
        connections = []
        for i in range(0, solution.n**2):
                for j in range(0, solution.n**2):
                    if solution.board[i,j]==solution.board[position[0],position[1]]:
                        equal_nodes.append("{}_{}".format(i,j))
                    elif solution.board[i,j]!=solution.board[position[0],position[1]] and solution.board[i,j]!=0:
                      filled_nodes.append("{}_{}".format(i,j))  
        for z in range(0,len(equal_nodes)):
            for m in range(z+1,len(equal_nodes)):
                for neighbor in self._graph[equal_nodes[m]]:
                    if not self.is_connected(node1=equal_nodes[z], node2=neighbor):
                        connections.append((equal_nodes[z],neighbor))
        for filled_node in filled_nodes:
            if not self.is_connected(node1=filled_node, node2="{}_{}".format(position[0],position[1])):
                        connections.append((filled_node,"{}_{}".format(position[0],position[1])))
        self.add_connections(connections)

    def get_value(self, row: int, column: int, solution: Board):
        print(solution.board)
        node = "{}_{}".format(row,column)
        possible_values = set(range(1,solution.n**2+1))
        connections = self._graph[node]
        print(node)
        print(connections)
        for connection in connections:
            position = self.get_row_and_column(connection)
            connection_value = solution.board[position[0]][position[1]]
            print(connection+"  discard  "+ str(connection_value))
            possible_values.discard(connection_value)
        print("possible values: "+str(possible_values))
        if(len(possible_values)==1):
            return list(possible_values)[0]
        else:
            return 0
    def get_row_and_column(self, node):
        return(int(node.split("_")[0]),int(node.split("_")[1]))