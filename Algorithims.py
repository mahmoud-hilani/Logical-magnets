from collections import deque

from heapq import heappop, heappush

from heapq import heappop, heappush


def ucs(initial_state):
    # Priority queue: stores (cost, state) tuples
    priority_queue = [initial_state]
    visited = set()
    visited.add(initial_state.layout_tuple())

    while priority_queue:
        state = heappop(priority_queue)

        if state.goal_state():
            return reconstruct_path(state)

        for move in state.possible_moves():
            new_state = state.apply_move(move)
            if new_state is None:  # Skip invalid states
                continue
            layout_tuple = new_state.layout_tuple()
            if layout_tuple not in visited:
                visited.add(layout_tuple)
                heappush(priority_queue,  new_state)
    return []


def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state.layout_tuple())

    while queue:
        state = queue.popleft()

        if state.goal_state():
            return reconstruct_path(state)

        for move in state.possible_moves():
            new_state = state.apply_move(move)

            layout_tuple = new_state.layout_tuple()
            if layout_tuple not in visited:
                visited.add(layout_tuple)
                queue.append(new_state)
    return []


def dfs(initial_state):
    stack = [initial_state]
    visited = set()
    visited.add(initial_state.layout_tuple())

    while stack:
        state = stack.pop()

        if state.goal_state():
            return reconstruct_path(state)

        if state.current_moves < state.max_moves:
            for move in state.possible_moves():
                new_state = state.apply_move(move)

                layout_tuple = new_state.layout_tuple()
                if layout_tuple not in visited:
                    visited.add(layout_tuple)
                    stack.append(new_state)

    return []


def reconstruct_path(goal_state):
    """Backtrack from the goal state to the initial state, returning a list of moves."""
    path = []
    state = goal_state
    while state.parent:
        path.append(state.last_move)
        state = state.parent
    path.reverse()
    return path
