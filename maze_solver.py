import heapq
# Maze Representation
maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'G', '.']
]
# Start and Goal Positions
start = (0, 0)
goal = (4, 3)

# Directions: Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search Algorithm
def astar(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    # Priority Queue
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Store path
    came_from = {}

    # Cost from start
    g_score = {start: 0}

    # Total cost
    f_score = {start: heuristic(start, goal)}

    visited = set()

    while open_set:

        current = heapq.heappop(open_set)[1]

        # Goal reached
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        visited.add(current)

        # Explore neighbors
        for direction in directions:

            row = current[0] + direction[0]
            col = current[1] + direction[1]

            neighbor = (row, col)

            # Check boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue

            # Check walls
            if maze[row][col] == '#':
                continue

            # Skip visited
            if neighbor in visited:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g_score

                f_score[neighbor] = (
                    tentative_g_score +
                    heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score[neighbor], neighbor)
                )

    return None


# Run A* Algorithm
path = astar(maze, start, goal)

if path:

    print("Shortest Path Found:\n")

    # Mark path in maze
    for position in path:

        row, col = position

        if maze[row][col] not in ['S', 'G']:
            maze[row][col] = '*'

    # Print maze
    for row in maze:
        print(" ".join(row))

    print("\nPath Coordinates:")
    print(path)

else:
    print("No path found!")