# stage.py

from board import Board

class Stage:
    def __init__(self, width, height, layout, target_positions, max_moves):
        self.board = Board(width, height, layout, target_positions)
        self.max_moves = max_moves
        self.current_moves = 0

    def play_move(self, start_row, start_col, dest_row, dest_col):
        if self.current_moves >= self.max_moves:
            print("No moves left!")
            return

        if self.board.move_magnet(start_row, start_col, dest_row, dest_col):
            self.current_moves += 1
            print(f"Move {self.current_moves}/{self.max_moves}")
            if self.goal_state():
                print("Congratulations! All target cells are filled. Goal state achieved!")
            # elif self.current_moves >= self.max_moves:
            #     print("You have reached the maximum number of moves for this stage!")
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
