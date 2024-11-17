# main.py
from Algorithims import *
from stages import STAGES
from state import State
from collections import deque



def play_moves(state, moves):
    state.display()
    for step in moves:
        state.play_move(step)


if __name__ == "__main__":
    initial_state = STAGES[4]
    

    path = ucs(initial_state)
    
    if path:
        print("Solution found! Playing moves:")
        play_moves(initial_state, path)
    else:
        print("No solution found.")


 # No solution found

# if __name__ == "__main__":
#     state = STATES[0]
#     state.display()
    
#     while state.current_moves < state.max_moves and not state.goal_state():
#         try:
#             start_row = int(input("Enter the row of the movable cell: ")) - 1
#             start_col = int(input("Enter the column of the movable cell: ")) - 1
#             dest_row = int(input("Enter the destination row: ")) - 1
#             dest_col = int(input("Enter the destination column: ")) - 1
            
#             state.play_move(start_row, start_col, dest_row, dest_col)
#             state.display()
            
#         except ValueError:
#             print("Please enter valid integer coordinates.")
#         except IndexError:
#             print("Coordinates out of bounds. Try again.")
#     if not state.goal_state():
#         print("You Lost")
