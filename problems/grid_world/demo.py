"""Demo script for grid world navigation system."""

from position import Position
from grid_world import GridWorld
from agent import Agent
from path import Pathfinder
import time


def main():
    """Run grid world navigation demo."""

    print("=" * 60)
    print("GRID WORLD NAVIGATION DEMO")
    print("=" * 60)

    # Build a 5×7 world
    world = GridWorld(rows=5, cols=7)

    # Set custom start and goal
    world.start = Position(0, 0)
    world.goal = Position(4, 6)

    # Add walls to create a maze
    walls = [
        Position(1, 1), Position(1, 2), Position(1, 3),
        Position(2, 3), Position(3, 3), Position(3, 1),
        Position(2, 5)
    ]

    for wall in walls:
        world.place_wall(wall)

    # Print initial world
    print("\nInitial Grid World:")
    print("Legend: S=start, G=goal, #=wall, .=empty")
    print("-" * 60)
    world.render()

    # Use BFS to find path
    print("\n" + "=" * 60)
    print("FINDING PATH WITH BFS...")
    print("=" * 60)

    pathfinder = Pathfinder(world)
    path = pathfinder.find_path(world.start, world.goal)

    if path is None:
        print("No path found from start to goal!")
        return

    print(f"\nPath found!")
    print(f"Path length: {len(path)} steps")
    print(f"Nodes expanded: {pathfinder.nodes_expanded}")

    # Print path coordinates
    print(f"\nPath: {' → '.join(str(p) for p in path)}")

    # Render path on grid
    print("\nGrid with Path (*):")
    print("-" * 60)
    world.render(path=path)

    # Step agent along path
    print("\n" + "=" * 60)
    print("STEPPING AGENT ALONG PATH...")
    print("=" * 60)

    agent = Agent(world)

    for i, position in enumerate(path):
        print(f"\nStep {i + 1}/{len(path)} - Agent at {position}")
        print("-" * 60)
        world.render(path=path, agent=position)

        if i < len(path) - 1:
            time.sleep(0.5)  # Pause for visualization

    print("\n" + "=" * 60)
    print("Agent reached the goal!")
    print("=" * 60)


if __name__ == "__main__":
    main()
