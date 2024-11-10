# main.py

from stage import State
from collections import deque

STAGES = [#0
    State(
        layout=[
            [".", "."],
            ["P", "G"],
            [".", "."],
          
        ],
        target_positions={(2, 1),(0, 1)},  # Pass target positions as a set
        max_moves=5
    ),    State(
        layout=[
            [".", ".",".","."],
            [".", ".","G","."],
            ["P", ".",".","."],
          
        ],
        target_positions={
                          (1, 1),(1, 3),
                          },  # Pass target positions as a set
        max_moves=3
    ),
    # 2
    State(
    layout=[
        [".", ".", ".", ".", "."],
        [".", ".", "G", "", "."],
        [".", "G", ".", "G", "."],
        ["P", ".", "G", ".", "."],
        [".", ".", ".", ".", "."],
    ],
    target_positions={
        (0, 2), (2, 0), (2,4), (2, 0), (4,2)
    },  # Only specify target positions here
    max_moves=2
),

    State(
        layout=[
            [".", "B","."],
            ["G", "B","G"],
            ["G", "B","G"],
            [".", "P","."],
          
        ],
        target_positions={(0, 0),(0, 2)
                          ,(1, 0),(1, 2),
                          (3,0)},  # Pass target positions as a set
        max_moves=2
    ),
    # 4
    State(
    layout=[
        ["B", "B", "B", "."],
        ["P", ".", "G", "."],
        [".", ".", ".", "."],
    ],
    target_positions={
        (0, 3), (2, 3)
    },  # Only specify target positions here
    max_moves=4
),
    State(
        layout=[
            [".", "B","."],
            ["G", "B","G"],
            ["G", "B","G"],
            [".", "P","."],
          
        ],
        target_positions={(0, 0),(0, 2)
                          ,(1, 0),(1, 2),
                          (3,0)},  # Pass target positions as a set
        max_moves=2
    ),
]

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state.layout_tuple())
    
    while queue:
        state = queue.popleft()
        
        if state.goal_state():
            return reconstruct_path(state)  # Return list of states or moves
        
        for move in state.possible_moves():
            new_state = state.apply_move(move)
            layout_tuple = new_state.layout_tuple()
            if layout_tuple not in visited:
                visited.add(layout_tuple)
                queue.append(new_state)
    return []  # No solution found

def dfs(initial_state):
    stack = [initial_state]
    visited = set()
    visited.add(initial_state.layout_tuple())
    
    while stack:
        state = stack.pop()
        
        if state.goal_state():
            return reconstruct_path(state)  # Return list of states or moves
        
        for move in state.possible_moves():
            new_state = state.apply_move(move)
            layout_tuple = new_state.layout_tuple()
            if layout_tuple not in visited:
                visited.add(layout_tuple)
                stack.append(new_state)
    return []  # No solution found

def reconstruct_path(goal_state):
    """Backtrack from the goal state to the initial state, returning a list of moves."""
    path = []
    state = goal_state
    while state.parent:  # Traverse until reaching the initial state (where parent is None)
        path.append(state)  # Alternatively, store (move) information if preferred
        state = state.parent
    path.reverse()
    return path

def play_moves(state, moves):
    """Play a sequence of moves on the given initial state."""
    for step in moves:
        step.display()  # Display each state


if __name__ == "__main__":
    initial_state = STAGES[2]
    
    # Find path using BFS or DFS
    path = dfs(initial_state)  # Or use dfs(initial_state)
    
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
