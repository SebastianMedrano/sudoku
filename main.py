from board import Board
from coloredGraph import ColoredGraphSolver
 
if __name__=="__main__":
    initial_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solved_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]



    
    # board = Board(3, initial_sudoku)
    # board2 = Board(3, initial_sudoku)
    # c = ColoredGraphSolution(board)
    # solution = c.implementation(board=board)
    # print("hola")
    # print(solution.board)
    # if (solution.board== solved_sudoku).all():
    #     print("solucionado")
    # else:
    #     print("error")


    board = Board(initial_sudoku)

    # Choose a solver (either ColoredGraphSolver or BacktrackingSolver)
    solver = ColoredGraphSolver(board)  # or use ColoredGraphSolver(board)

    # Solve the Sudoku
    try:
        solution = solver.solve()
        print("Solved Sudoku:")
        for row in solution:
            print(row)
    except ValueError as e:
        print(str(e))
