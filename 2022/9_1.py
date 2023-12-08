filename = "resources/day_9_input.txt"
#filename = "resources/debug.txt"

import math


def move(head_pos, tail_pos, head_direction, steps, tail_visited):
    tail_dir = get_opposite(head_direction)
    for c in range(steps):
        if head_direction == 'L':
            head_pos[1] += -1
        elif head_direction == 'R':
            head_pos[1] += +1
        elif head_direction == 'U':
            head_pos[0] += +1
        elif head_direction == 'D':
            head_pos[0] += -1
        if tail_req_move(head_pos, tail_pos):
            tail_pos = move_tail(head_pos, tail_pos, tail_dir)
            tail_visited = update_tail_visited_position(tail_visited, tail_pos)
        print(f'Head pos {head_pos}, Tail pos {tail_pos}')

    return head_pos, tail_pos


def tail_req_move(head_pos, tail_post):
    dist = math.dist(head_pos, tail_post)
    return True if dist >= 2 else False


def get_opposite(head_dir):
    if head_dir == 'L':
        return 'R'
    elif head_dir == 'R':
        return 'L'
    elif head_dir == 'U':
        return 'D'
    elif head_dir == 'D':
        return 'U'


def move_tail(head_pos, tail_pos, tail_direction):
    if tail_direction == 'L':
        tail_pos[0] = head_pos[0]
        tail_pos[1] = head_pos[1] - 1
    elif tail_direction == 'R':
        tail_pos[0] = head_pos[0]
        tail_pos[1] = head_pos[1] + 1
    elif tail_direction == 'U':
        tail_pos[0] = head_pos[0] + 1
        tail_pos[1] = head_pos[1]
    elif tail_direction == 'D':
        tail_pos[0] = head_pos[0] - 1
        tail_pos[1] = head_pos[1]
    return tail_pos


def update_tail_visited_position(tail_visited, tail_pos):
    t = (tail_pos[0], tail_pos[1])
    tail_visited.add(t)
    return tail_visited


def resolve():
    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_visited = set()
    tail_visited.add((tail_pos[0], tail_pos[1]))
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            direction = line.split(' ')[0]
            steps = int(line.split(' ')[1])
            head_pos, tail_pos = move(head_pos, tail_pos, direction, steps, tail_visited)

    return len(tail_visited)


print(resolve())
