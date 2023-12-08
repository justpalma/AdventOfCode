filename = 'resources/day_12_input.txt'
#filename = 'resources/debug.txt'
from collections import deque


def find_min_path(matrix, start, target):
    visited = {start}
    todo = deque([(start, 0)])
    c = 0
    while todo:
        (cx, cy), d = todo.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and (nx, ny) not in visited
                and grid[ny][nx] <= grid[cy][cx] + 1
            ):
                if (nx, ny) == target:
                    return d + 1
                todo.append(((nx, ny), d + 1))
                visited.add((nx, ny))
    return float("inf")


with open(filename) as file:
    grid = [list(line) for line in file.read().splitlines()]

    starts = []
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                starts.append((x, y))
                start = (x, y)
                grid[y][x] = ord("a")
            elif c == 'E':
                target = (x, y)
                grid[y][x] = ord("a")
            else:
                if c == "a":
                    starts.append((x, y))
                grid[y][x] = ord(c)

print(grid)
print(start)
print(starts)
print(target)

print(find_min_path(grid, start, target))
