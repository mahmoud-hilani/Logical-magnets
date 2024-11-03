    # board.py

from cell import *

class Board:
    def __init__(self, width, height, layout, target_positions):
        self.width = width
        self.height = height
        self.grid = [[{"piece": None} for _ in range(width)] for _ in range(height)]
          # Use set for to search fast and if cell and target in the same place
        self.target_positions = set(target_positions) 
        self.load_layout(layout)

    def load_layout(self, layout):
        for i, row in enumerate(layout):
            for j, cell in enumerate(row):
                if cell == "R":
                    self.grid[i][j]["piece"] = RedCell()
                elif cell == "P":
                    self.grid[i][j]["piece"] = PurpleCell()
                elif cell == "G":
                    self.grid[i][j]["piece"] = GrayCell()
                elif cell == "B":
                    self.grid[i][j]["piece"] = Block()

    def is_within_bounds(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width

    def get_piece(self, x, y):
        return self.grid[x][y]["piece"]

    def is_empty(self, x, y):
        return self.is_within_bounds(x, y) and self.grid[x][y]["piece"] is None

    def is_target(self, x, y):
        return (x, y) in self.target_positions

    def move_piece(self, from_x, from_y, to_x, to_y):
        if self.is_empty(to_x, to_y):
            self.grid[to_x][to_y]["piece"] = self.grid[from_x][from_y]["piece"]
            self.grid[from_x][from_y]["piece"] = None

    def move_magnet(self, start_row, start_col, dest_row, dest_col):
        cell = self.grid[start_row][start_col]["piece"]
        if isinstance(cell, MovableCell) and self.grid[dest_row][dest_col]["piece"] is None:
            self.grid[start_row][start_col]["piece"] = None
            self.grid[dest_row][dest_col]["piece"] = cell
            cell.interact_with(self, dest_row, dest_col)
            return True
        return False 


        

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                piece = self.get_piece(i, j)
                if piece:
                    print(piece, end=" ")
                elif self.is_target(i, j):
                    print("T", end=" ")
                else:
                    print(".", end=" ")
            print()
        print("\n")
