# cell.py

from abc import ABC, abstractmethod

class Cell:
    def __str__(self):
        return "."  
class MovableCell(Cell, ABC):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @abstractmethod
    def interact_with(self, board, x, y):
        pass

class RedCell(MovableCell):
    def interact_with(self, board, x, y):
        for dx, dy in self.directions:
            self.attract_recursive(board, x, y, dx, dy)

    def attract_recursive(self, board, x, y, dx, dy):
        current_x, current_y = x + dx, y + dy
        while board.is_within_bounds(current_x, current_y):
            cell = board.get_piece(current_x, current_y)
            if cell is None:
                current_x += dx
                current_y += dy
            elif isinstance(cell, Block):
                return
            else:
                self.pull_cell(board, current_x, current_y, dx, dy)
                current_x += dx
                current_y += dy

    def pull_cell(self, board, x, y, dx, dy):
        new_x, new_y = x - dx, y - dy
        if board.is_empty(new_x, new_y):
            board.move_piece(x, y, new_x, new_y)

    def __str__(self):
        return "R"

class PurpleCell(MovableCell):
    def interact_with(self, board, x, y):
        for dx, dy in self.directions:
            self.push_recursive(board, x, y, dx, dy)

    def push_recursive(self, board, x, y, dx, dy):
        current_x, current_y = x + dx, y + dy
        while board.is_within_bounds(current_x, current_y):
            if board.is_empty(current_x, current_y) :
                current_x += dx
                current_y += dy
            elif isinstance(board.get_piece(current_x, current_y), Block):
                return
            else:
                self.push_cells(board, current_x, current_y, dx, dy)
                return


    def push_cells(self, board, x, y, dx, dy):
        next_x, next_y = x + dx, y + dy

        if not board.is_within_bounds(next_x, next_y):
            return False  

        if board.is_empty(next_x, next_y):
            board.move_piece(x, y, next_x, next_y)
            return True  
        else:
            if self.push_cells(board, next_x, next_y, dx, dy):

                board.move_piece(x, y, next_x, next_y)
                return True
        return False  
    # def push_cell(self, board, x, y, dx, dy):
    #     next_x, next_y = x + dx, y + dy
    #     if board.is_within_bounds(next_x, next_y) and board.is_empty(next_x, next_y):
    #         board.move_piece(x, y, next_x, next_y)

    def __str__(self):
        return "P"

class GrayCell(Cell):
    def __str__(self):
        return "G"

class Block(Cell):
    def __str__(self):
        return "B"
