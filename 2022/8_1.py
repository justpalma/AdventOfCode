filename = "resources/day_8_input.txt"
#filename = "resources/debug.txt"


def load_matrix():
    m = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            m.append(list(line))

    return m, len(m)


def analyze_list(l, v):
    """
    Verifica che nella lista l(che è una subriga o subcolonna) il nostro valore(v) sia visibile
    :param l:
    :param v:
    :return:
    """
    # ordino la lista dal più grande al più piccolo
    l = sorted(l, reverse=True)
    # se il nostro valore è in prima posizione ed è l'unico, allora è visibile
    if l[0] == v and l.count(v) == 1:
        return True
    else:
        return False


def compose_column_list(m, y_start, y_stop, x):
    """
    Compone lista per le colonne.
    La notazione m[0:c_y][c_x] non si può usare per le colonne perchè sono object diversi
    """
    l = []
    if y_start > y_stop:
        y_start, y_stop = y_stop, y_start
    for y in range(y_start, y_stop):
        l.append(m[y][x])
    return l


def is_visible(m, processed, c_y, c_x, size):
    index = str(c_y) + str(c_x)
    value = m[c_y][c_x]
    if index in processed:
        return False
    else:
        if c_y == 0 or c_y == size or c_x == 0 or c_x == size:
            # è un albero esterno, è sempre visibile
            processed.add(index)
            return True

        if analyze_list(m[c_y][0:c_x + 1], value):
            return True

        if analyze_list(m[c_y][c_x:size], value):
            return True

        if analyze_list(compose_column_list(m, 0, c_y + 1, c_x), value):
            return True

        if analyze_list(compose_column_list(m, c_y, size, c_x), value):
            return True

        return False


MATRIX, size = load_matrix()


def resolve():
    total_visible = 0
    processed = set()
    for y in range(size):
        for x in range(size):
            if is_visible(MATRIX, processed, y, x, size):
                total_visible += 1
    return total_visible


print(resolve())
