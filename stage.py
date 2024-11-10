# stage.py

from board import Board
from cell import MovableCell  # Import MovableCell and any other necessary classes here
from copy import deepcopy

class State:
    def __init__(self, layout, target_positions, max_moves, parent=None):
        self.height = len(layout)
        self.width = len(layout[0]) if layout else 0
        self.board = Board(self.width, self.height, layout, target_positions)
        self.max_moves = max_moves
        self.current_moves = 0
        self.parent = parent  # Add a parent state for backtracking

    def play_move(self, start_row, start_col, dest_row, dest_col):
        if self.current_moves >= self.max_moves:
            print("No moves left!")
            return

        if self.board.move_magnet(start_row, start_col, dest_row, dest_col):
            self.current_moves += 1
            print(f"Move {self.current_moves}/{self.max_moves}")
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
                # Check if the current cell contains a movable piece
                if isinstance(piece, MovableCell):
                    # Find all empty cells on the board where this piece could move
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

        
        
        new_state = deepcopy(self)
        new_state.parent = self  # Set current state as the parent of the new state
        print(f"Applying move: ({start_row}, {start_col}) -> ({end_row}, {end_col})")




        # Apply the move in the new state
        if new_state.board.move_magnet(start_row, start_col, end_row, end_col):
            new_state.current_moves += 1
        return new_state

    def layout_tuple(self):
        """Return a hashable tuple representation of the board layout."""
        # Create a tuple of tuples from the grid for hashable representation
        return tuple(tuple(cell for cell in row) for row in self.board.grid)
