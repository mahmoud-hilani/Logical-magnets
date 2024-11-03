# main.py

from stage import Stage

STAGES = [
    Stage(
        width=5,
        height=5,
        layout=[
            [".", ".", "G", ".", "."],
            ["G", "G", ".", "B", "."],
            ["G", ".", "G", ".", "."],
            [".", ".", "R", ".", "."],
            ["P", ".", ".", ".", "R"]
        ],
        target_positions={(0, 4), (4, 0)},  # Pass target positions as a set
        max_moves=5
    ),
]

if __name__ == "__main__":
    stage = STAGES[0]
    stage.display()
    
    while stage.current_moves < stage.max_moves and not stage.goal_state():
        try:
            start_row = int(input("Enter the row of the movable cell: "))-1
            start_col = int(input("Enter the column of the movable cell: "))-1
            dest_row = int(input("Enter the destination row: "))-1
            dest_col = int(input("Enter the destination column: "))-1
            
            stage.play_move(start_row, start_col, dest_row, dest_col)
            stage.display()
            
        except ValueError:
            print("Please enter valid integer coordinates.")
        except IndexError:
            print("Coordinates out of bounds. Try again.")
    if not stage.goal_state():
        print("You Lost ")