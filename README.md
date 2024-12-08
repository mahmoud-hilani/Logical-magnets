
# Logical Magnets

Most OOP principles have been employed in this project.

## 1. State Description

The state represents the board. It contains a two-dimensional array to represent all cells, including `Blocks`. The target cells are represented by a list. The state also keeps track of the current move count, the maximum allowed moves, and the parent state from which this state was derived. It converts a character array into a `Board` object.

## 2. State Space

The state space includes all possible configurations of cells on the board that can be reached through valid moves. By applying the available operations, we generate new states from existing ones, representing all positions reachable within the allowed number of moves.

## 3. Initial State

The initial state is defined by how cells are distributed on the board at the start of the game. This determines the initial position of each cell based on the given layout, as well as which target positions must be filled. In the code, this distribution is represented by a specific `Stage`, and the search begins from this initial configuration.

## 4. Operations and Procedures

Operations include all the permissible moves that movable cells can perform. For example, red and purple objects have methods to move cells by either pushing or pulling them, depending on the type. These operations are carried out through functions like `move_piece` and `move_magnet`, which handle cell relocation within the grid and validate constraints—such as ensuring that the moved cell is movable and the destination is free.

## 5. Final State

The final state is reached when all target positions (as defined in `target_positions`) are correctly occupied by the required cells. The `goal_state` function checks whether all target spots are filled properly. If this condition is met, the objective is considered achieved and the solution is found.

## Polymorphism is Used

Polymorphism is utilized for movable cells—those that the user can manipulate, such as purple and red cells. The `Movable` class includes the `InteractWith` method, allowing magnets to interact appropriately with other cells.

## Improvements

- To simplify the addition of new stages, a function was created to convert a character array into cells.
- For improved efficiency, the `visited` array in BFS and DFS algorithms stores a two-dimensional array of characters rather than storing entire cell objects.
