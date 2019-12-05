"""
Base definition of the Sudoku board and associated information, such as individuals and fitness function.
"""
import numpy.random as rand


class BoardFormatException(Exception):
    pass

class Sudoku:
    def __init__(self, starting_grid):
        """
        Expects a list with numbers in the INITIAL board written sequentially from top to bottom and left to right.
        Empty positions should have value None. Boards should be square.
        """
        try:
            if any([len(starting_grid) != len(starting_grid[i]) for i in range(len(starting_grid))]):
                raise BoardFormatException
        except (TypeError, IndexError):
            raise

        self.grid = starting_grid
        self.locked_positions = set() 
        for i in range(len(starting_grid)):
            for j in range(len(starting_grid[i])):
                if starting_grid[i][j] is not None:
                    self.locked_positions.add((i,j))

    def __str__(self):
        rep = ""
        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                if self.grid[i][j] is None:
                    s = "-"
                else:
                    s = str(self.grid[i][j])
                rep = rep + s + " "
            rep += "\n"

        return rep

    def generate_new_individual(self):
        """
        Creates an entirely new individual from a starting grid, skipping locked positions.
        """
        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                if (i,j) not in self.locked_positions:
                    self.grid[i][j] = rand.randint(1,10)

    # def disturb(self):
    #     """
    #     Creates a new individual by introducing a minor disturbance in the board
    #     """