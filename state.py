from board import Board
from cell import MovableCell, GrayCell
from copy import deepcopy

class State:
    def __init__(self, layout, target_positions, max_moves, parent=None, last_move=None):
        self.height = len(layout)
        self.width = len(layout[0]) if layout else 0
        self.board = Board(self.width, self.height, layout, target_positions)
        self.max_moves = max_moves
        self.current_moves = 0
        self.parent = parent  
        self.last_move = last_move 



    def play_move(self, move):

        start_pos, end_pos = move
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if self.current_moves >= self.max_moves:
            print("No moves left!")
            return

        if self.board.move_magnet(start_row, start_col, end_row, end_col):
            self.current_moves += 1
            self.display()
            if self.goal_state():
                print("Congratulations! All target cells are filled. Goal state achieved!")
        else:
            print("Invalid move. Either the cell is not movable, or the destination is not empty.")

    def goal_state(self):
        for x, y in self.board.target_positions:
            if self.board.get_piece(x, y) is None:
                return False
        return True

    def display(self):
        print(f"Current Move: {self.current_moves}/{self.max_moves}")
        self.board.display()

    def possible_moves(self):
        """Generate all possible moves by pairing each movable piece with every empty cell."""
        moves = []
        for row in range(self.board.height):
            for col in range(self.board.width):
                piece = self.board.get_piece(row, col)

                if isinstance(piece, MovableCell):

                    for target_row in range(self.board.height):
                        for target_col in range(self.board.width):
                            if self.board.is_empty(target_row, target_col):
                                moves.append(((row, col), (target_row, target_col)))
        return moves

    def apply_move(self, move):
        """Apply a move to create a new state, with this state as its parent."""
        start_pos, end_pos = move
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        if self.current_moves >= self.max_moves:
            print("No moves left!")
            return
        
        new_state = deepcopy(self)
        new_state.parent = self 
        new_state.last_move = move  
        print(f"Applying move: ({start_row}, {start_col}) -> ({end_row}, {end_col})")


        if new_state.board.move_magnet(start_row, start_col, end_row, end_col):
            new_state.current_moves += 1
        return new_state

    def layout_tuple(self):
        return tuple(tuple(cell for cell in row) for row in self.board.grid)

    def heuristic(self):
            # the heuristic function is finding the
            # max distance of a magnet to the target
            # :) the minimum steps to the target
            max_distance = 0

            for row in range(self.board.height):
                for col in range(self.board.width):
                    piece = self.board.get_piece(row, col)
                    if isinstance(piece, GrayCell):  # Only consider movable pieces
                                    # inf means infinity
                        min_distance = float('inf')
                        for target_row, target_col in self.board.target_positions:
                            distance = abs(target_row - row) + abs(target_col - col)
                            min_distance = min(min_distance, distance)
                        max_distance = max(max_distance, min_distance)

            return max_distance

        # less than for the queue
    def __lt__(self, other):
        self_cost = self.current_moves
        other_cost = other.current_moves
        self_heuristic = self.heuristic()
        other_heuristic = other.heuristic()
        # print(f"Self heuristic: {self_heuristic}")
        # print(f"Other heuristic: {other_heuristic}")


        return self_cost  < other_cost

        # return self_heuristic < other_heuristic

        # return self_cost + self_heuristic < other_cost + other_heuristic

