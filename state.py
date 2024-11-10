from board import Board
from cell import MovableCell , RedCell, GrayCell,PurpleCell,Block
from copy import deepcopy

class State:
    def __init__(self, layout, target_positions, max_moves, parent=None):
        self.height = len(layout)
        self.width = len(layout[0]) if layout else 0
        self.layout = layout  # Store layout
        self.target_positions = target_positions
        self.max_moves = max_moves
        self.current_moves = 0
        self.parent = parent  # For backtracking

    def _create_board(self):
        """Create and return a new board based on current state layout and target_positions."""
        return Board(self.width, self.height, self.layout, self.target_positions)

    def update_layout_from_board(self, board):
        """Update the layout to reflect the current board grid."""
        self.layout = []
        for row in range(board.height):
            layout_row = []
            for col in range(board.width):
                piece = board.get_piece(row, col)
                if isinstance(piece, RedCell):
                    layout_row.append("R")
                elif isinstance(piece, PurpleCell):
                    layout_row.append("P")
                elif isinstance(piece, GrayCell):
                    layout_row.append("G")
                elif isinstance(piece, Block):
                    layout_row.append("B")
                else:
                    layout_row.append(None)  # Empty cell
            self.layout.append(layout_row)

    def play_move(self, start_row, start_col, dest_row, dest_col):
        if self.current_moves >= self.max_moves:
            print("No moves left!")
            return

        board = self._create_board()  # Create the board when needed
        print(f"Attempting move: ({start_row}, {start_col}) -> ({dest_row}, {dest_col})")
        
        if board.move_magnet(start_row, start_col, dest_row, dest_col):
            self.current_moves += 1
            self.update_layout_from_board(board)  # Sync the layout with the board
            print(f"Move {self.current_moves}/{self.max_moves}")
            if self.goal_state():
                print("Congratulations! All target cells are filled. Goal state achieved!")
        else:
            print("Invalid move. Either the cell is not movable, or the destination is not empty.")

    def goal_state(self):
        board = self._create_board()  # Create board when checking goal state
        print("Checking goal state...")
        for x, y in self.target_positions:
            if board.get_piece(x, y) is None:
                print(f"Goal not reached: Target ({x}, {y}) is empty.")
                return False
        print("Goal state achieved!")
        return True

    def display(self):
        print(f"Current Move: {self.current_moves}/{self.max_moves}")
        board = self._create_board()  # Create board to display
        board.display()

    def possible_moves(self):
        """Generate all possible moves by pairing each movable piece with every empty cell."""
        moves = []
        board = self._create_board()  # Create board to check available moves
        print("Generating possible moves...")

        for row in range(board.height):
            for col in range(board.width):
                piece = board.get_piece(row, col)
                if isinstance(piece, MovableCell):  # If it's a movable piece
                    for target_row in range(board.height):
                        for target_col in range(board.width):
                            if board.is_empty(target_row, target_col):  # Target must be empty
                                moves.append(((row, col), (target_row, target_col)))
        print(f"Possible moves: {moves}")
        return moves

    def apply_move(self, move):
        """Apply a move to create a new state, with this state as its parent."""
        start_pos, end_pos = move
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        new_state = deepcopy(self)
        new_state.parent = self  # Set current state as parent of new state

        # Ensure the board is correctly initialized in the new state
        board = new_state._create_board()  # Initialize the board for the new state
        print(f"Applying move: ({start_row}, {start_col}) -> ({end_row}, {end_col})")
        if board.move_magnet(start_row, start_col, end_row, end_col):
            new_state.current_moves += 1
            new_state.update_layout_from_board(board)
            return None  # Update the layout after the move
        return new_state

    def layout_tuple(self):
        """Return a hashable tuple representation of the board layout."""
        return tuple(tuple(cell for cell in row) for row in self.layout)
