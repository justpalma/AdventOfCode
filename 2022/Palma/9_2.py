import math
import matplotlib.pyplot as plt

#filename = "resources/debug.txt"
filename = "resources/day_9_input.txt"

direction_object = {
    'L': 8,
    'R': 7,
    'U': 5,
    'D': 6,
    'UL': 1,
    'UR': 2,
    'DL': 3,
    'DR': 4,
}


class Point(object):
    def __init__(self, x=0, y=0):
        self._c = [x, y]

    @property
    def cord(self):
        return list(self._c)

    @property
    def x(self):
        return self._c[0]

    @property
    def y(self):
        return self._c[1]

    @x.setter
    def x(self, value):
        self._c[0] = value

    @y.setter
    def y(self, value):
        self._c[1] = value

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x += -1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y += -1

    def move_up_left(self):
        self.y += 1
        self.x += -1

    def move_up_right(self):
        self.y += 1
        self.x += 1

    def move_down_left(self):
        self.y += -1
        self.x += -1

    def move_down_right(self):
        self.y += -1
        self.x += 1

    def __str__(self):
        return f"X:{self.x} Y:{self.y}"


def touching(p1: Point, p2: Point):
    dist = math.dist(p1.cord, p2.cord)
    return False if dist >= 2 else True


def same_column(p1: Point, p2: Point):
    return True if p1.x == p2.x else False


def same_row(p1: Point, p2: Point):
    return True if p1.y == p2.y else False


def move_point(rope: list[Point], direction: int, index: int):
    if direction == direction_object['L']:
        rope[index].move_left()
    if direction == direction_object['R']:
        rope[index].move_right()
    if direction == direction_object['U']:
        rope[index].move_up()
    if direction == direction_object['D']:
        rope[index].move_down()
    if direction == direction_object['UL']:
        rope[index].move_up_left()
    if direction == direction_object['UR']:
        rope[index].move_up_right()
    if direction == direction_object['DL']:
        rope[index].move_down_left()
    if direction == direction_object['DR']:
        rope[index].move_down_right()

    return rope


def find_direction(p1: Point, p2: Point):
    """
    p1: usato per confronto
    p2: si deve spostare
    """
    if p1.x == p2.x:
        if p1.y > p2.y:
            return direction_object['U']  # UP same column
        else:
            return direction_object['D']  # DOWN same column
    elif p1.y == p2.y:
        if p1.x > p2.x:
            return direction_object['R']  # RIGHT same row
        else:
            return direction_object['L']  # LEFT same row

    elif p1.x > p2.x and p1.y > p2.y:
        return direction_object['UR']
    elif p1.x > p2.x and p1.y < p2.y:
        return direction_object['DR']
    elif p1.x < p2.x and p1.y > p2.y:
        return direction_object['UL']
    elif p1.x < p2.x and p1.y < p2.y:
        return direction_object['DL']


def update_tail_position(rope, visited):
    visited.add((rope[9].x, rope[9].y))
    return visited


def move(rope, direction, steps, visited):
    for _ in range(steps):
        # sposto la testa
        rope = move_point(rope, direction, 0)

        for index in range(len(rope)):
            if index == 9:
                break
            if not touching(rope[index], rope[index + 1]):
                # punti non si toccano, vanno spostati
                movement_dir = find_direction(rope[index], rope[index + 1])
                rope = move_point(rope, movement_dir, index + 1)
                visited = update_tail_position(rope, visited)

    print(f'head pos {rope[0]}')
    return rope, visited


def resolve():
    total_obj = 1 + 9
    rope = []
    tail_visited = set()
    tail_visited.add((0, 0))
    for x in range(total_obj):
        p = Point()
        rope.append(p)

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            direction = line.split(' ')[0]
            steps = int(line.split(' ')[1])
            rope, tail_visited = move(rope, direction_object[direction], steps, tail_visited)

    return tail_visited


point = resolve()
print(len(resolve()))

# NOT REQUIRED BUT WHY NOT
fig, ax = plt.subplots()

for p in point:
    p_list = list(p)
    ax.scatter(p[0], p[1], c='r')

plt.show()
