# Grid World Navigation
Build a simple **grid world navigation system**. You will create classes to represent positions, a world with walls, an agent that moves, and a pathfinder that can find the shortest path from a start to a goal.

Organize your project as follows: 
```
grid_world/
├── position.py          # Position(row, col): neighbors_4, eq/hash, repr
├── grid_world.py        # GridWorld(rows, cols, walls, start, goal): in_bounds, passable, render
├── agent.py             # Agent(world, pos): step(up/down/left/right), can_move_to, reset
├── path.py               # Pathfinder(world): find_path(start, goal), expanded count
├── demo.py              # Script: build world, run BFS, render path, step agent
├── README.md            # Brief usage and assignment instructions
└── tests/               # simple unit tests
    ├── test_position.py
    ├── test_grid_world.py
    ├── test_agent.py
    └── test_bfs.py
```