from state import State

STAGES = [  # 0
    State(
        layout=[
            [".", "."],
            ["P", "G"],
            [".", "."],

        ],
        target_positions={(2, 1), (0, 1)},
        max_moves=5
    ), State(
        layout=[
            [".", ".", ".", "."],
            [".", ".", "G", "."],
            ["P", ".", ".", "."],

        ],
        target_positions={
            (1, 1), (1, 3),
        },
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
            (0, 2), (2, 0), (2, 4), (2, 0), (4, 2)
        },
        max_moves=2
    ),

    State(
        layout=[
            [".", "B", "."],
            ["G", "B", "G"],
            ["G", "B", "G"],
            [".", "P", "."],

        ],
        target_positions={(0, 0), (0, 2)
            , (1, 0), (1, 2),
                          (3, 0)},
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
        },
        max_moves=4
    ),
    State(
        layout=[
            [".", "B", "."],
            ["G", "B", "G"],
            ["G", "B", "G"],
            [".", "P", "."],

        ],
        target_positions={(0, 0), (0, 2)
            , (1, 0), (1, 2),
                          (3, 0)},
        max_moves=2
    ),
]

