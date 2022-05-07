"""
Sudoku Solver by Alan Shiah
Uses backtracking algorithm
Call stack
Return a value so the previous call can complete on completion of
state space tree nodes
Otherwise, stack overflow
"""
from tools.functions import sudoku_solver, display_board

if sudoku_solver(0, 0):
    display_board()
else:
    print("Unsolvable Puzzle")
