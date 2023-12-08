filename = "resources/day_8_input.txt"


def load_matrix():
    m = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            m.append(list(line))

    return m, len(m)





def how_many_visible_tree(m, c_y, c_x, size):
    spotted_left = 0
    spotted_right = 0
    spotted_up = 0
    spotted_down = 0

    value = m[c_y][c_x]
    # sinistra
    if c_x == 0:
        spotted_left = 0
    else:
        for x in range(c_x-1, -1, -1):
            v = m[c_y][x]
            if value > v:
                spotted_left += 1
            else:
                spotted_left += 1
                break

    # destra

    if c_x == size -1:
        spotted_right = 0
    else:
        for x in range(c_x+1, size):
            v = m[c_y][x]
            if value > v:
                spotted_right += 1
            else:
                spotted_right += 1
                break

    # sotto

    if c_y == size -1:
        spotted_down = 0
    else:
        for y in range(c_y+1, size):
            v = m[y][c_x]
            if value > v:
                spotted_down += 1
            else:
                spotted_down += 1
                break

    if c_y == 0:
        spotted_up = 0
    else:
        for y in range(c_y-1, -1, -1):
            v = m[y][c_x]
            if value > v:
                spotted_up += 1
            else:
                spotted_up += 1
                break

    print(f'indice {str(c_y)+str(c_x)} - valore {value} vede sinistra: {spotted_left}, destra: {spotted_right}, sopra: {spotted_up}, sotto: {spotted_down}')
    return spotted_up * spotted_left * spotted_down * spotted_right


MATRIX, size = load_matrix()


def resolve():
    l = []
    for y in range(size):
        for x in range(size):
            l.append(how_many_visible_tree(MATRIX, y, x, size))
    print(l)
    return max(l)


print(resolve())
