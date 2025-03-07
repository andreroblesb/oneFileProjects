"""
We will solve sudokus using a search algorithm with satisfaction restrictions. These are problems which often involve heuristics as well as combinatorics.

The problem to solve is a sudoku. Where we have a set of variables, constraints and domains. We could use the two type of approaches we have been using in other problems, either exhaustive methods like BFS or incomplete (local search) methods. We can also approach CSPs with state-based models (eg. backtracking) or variable-based models (arc-consistency).

In this case, we will use backtracking, which ensures a solution (if there is one), because we have a finite number of posibilities which my engineer hunch tells me is computationally possible in sudoku.

Variables: The empty squares
Domain: Numbers 1 to 9
Constraints:
- No number can be repeated along a horizontal line.
- No number can be repeated along a vertical line.
- No number can be repeated inside the marked 3x3 squares.

Backtracking is, in a sense, similar to the DFS (for graphs) algorithm. Backtracking is the general technique.

Problem is asumed to handle the classical 9x9 sudoku, which you will notice by some code lines (eg. 32).

"""
import copy

class State():
    def __init__(self, matrix):
        self.matrix : list[list[int]] = matrix
    
    def find_next(self):
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element == 0:
                    return (i, j)
                    
    def assign(self, move : tuple, n):
        self.matrix[move[0]][move[1]] = n
        return
    
    def remove(self, move: tuple):
        self.matrix[move[0]][move[1]] = 0
        return
    
    def check_constraints(self, move, n):
        
        # see if already assigned
        if self.matrix[move[0]][move[1]] != 0:
            # print("asignado")
            return False
        # horizontal check
        for x in self.matrix[move[0]]:
            # print("horizontal")
            if x == n:
                return False
        # vertical check
        for row in self.matrix:
            # print("vertical")
            if row[move[1]] == n:
                return False
        
        # 3x3 box check, checa que el 0 da igual
        box_start = ((move[0] // 3) * 3, (move[1] // 3) * 3)

        # Check the entire 3x3 box
        for i in range(3):
            for j in range(3):
                row, col = box_start[0] + i, box_start[1] + j
                if (row, col) != (move[0], move[1]) and self.matrix[row][col] == n:
                    return False
        return True

class Backtracking():
    def __init__(self, state):
        self.solution = state
    
    def solve(self, state : State):
        
        move = state.find_next()
        if move == None:
            print("solved!")
            self.solution = state
            return True
        
        for n in range(1, 10):
            if state.check_constraints(move, n):
                print("assigning", move, n)
                state.assign(move, n)
                new_state = copy.deepcopy(state)
                if self.solve(new_state):
                    return True
                state.remove(move)
        
        return False
    
    def __str__(self):
        string = ""
        iterable = self.solution.matrix
        for row in iterable:
            string += str(row) +"\n"
        return string

def main():
    sudoku1 = [[9, 3, 6, 0, 2, 5, 0, 1, 4], [0, 1, 7, 0, 3, 4, 9, 2, 8], [8, 0, 0, 0, 9, 7, 0, 0, 0], [0, 0, 3, 4, 0, 0, 5, 9, 0], [6, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 3, 8, 0, 0, 7, 1], [0, 0, 0, 9, 0, 0, 0, 0, 5], [0, 5, 1, 0, 4, 0, 0, 0, 0], [4, 6, 0, 0, 0, 0, 1, 8, 0]]
    
    sudoku2 = [[0, 0, 0, 8, 0, 7, 9, 1, 0], [9, 0, 0, 3, 4, 0, 2, 0, 0], [0, 0, 5, 0, 0, 0, 0, 7, 0], [5, 9, 3, 7, 0, 2, 0, 6, 4], [0, 0, 1, 0, 0, 0, 0, 3, 8], [8, 7, 0, 6, 3, 1, 0, 9, 2], [7, 4, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 4, 3, 0, 0], [0, 5, 2, 1, 7, 0, 0, 0, 0]]
    
    sudoku3 = [[5, 0, 0, 6, 9, 4, 0, 3, 2], [0, 0, 0, 3, 0, 7, 0, 0, 0], [9, 3, 6, 0, 1, 2, 0, 4, 0], [0, 0, 5, 2, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 1, 0, 0, 9], [2, 0, 8, 0, 0, 3, 5, 0, 0], [0, 6, 2, 0, 3, 0, 0, 0, 4], [3, 8, 1, 0, 4, 6, 0, 5, 0], [4, 0, 0, 7, 0, 8, 6, 1, 0]]
    
    sudoku4 = [[8, 7, 0, 0, 4, 2, 9, 1, 5], [1, 3, 0, 5, 0, 8, 0, 2, 0], [5, 0, 2, 0, 0, 0, 0, 8, 3], [4, 0, 3, 0, 0, 0, 8, 7, 0], [0, 6, 7, 0, 0, 1, 3, 0, 0], [0, 0, 0, 0, 0, 0, 2, 5, 0], [0, 0, 4, 6, 0, 5, 0, 3, 0], [6, 0, 1, 0, 0, 4, 5, 0, 8], [0, 8, 0, 2, 0, 0, 0, 0, 4]]
    
    state = State(sudoku4)
    solver = Backtracking(state)
    solver.solve(state)
    print(solver)
    return

if __name__ == "__main__":
    main()


