from functools import reduce

from loguru import logger


def is_number(val):
    return val.isnumeric()


matrix = []
with open("input.txt") as f:
    for line in f:
        matrix.append(list(line.replace("\n", "")))

for l in matrix:
    print(l)

c = len(matrix[0])
r = len(matrix)

print("#######")

tmp = ["." for _ in range(c)]
matrix.insert(0, tmp)
matrix.insert(c + 1, tmp)

for i in range(c + 1):
    matrix[i].insert(0, ".")
    matrix[i].insert(c + 1, ".")

print("#######")
for l in matrix:
    print(l)

curr_number = ""

c = len(matrix[0])
r = len(matrix)
new_total = 0

for x in range(c):
    for y in range(r):
        if (is_number(matrix[x][y])):
            curr_number += matrix[x][y]
        else:
            # non è un numero
            if curr_number:
                sub_matrix = []
                # print(curr_number)
                # print(x,y)
                sub_matrix.append(matrix[x - 1][(y - len(curr_number) - 1): y + 1])
                sub_matrix.append(matrix[x][(y - len(curr_number) - 1): y + 1])
                sub_matrix.append(matrix[x + 1][(y - len(curr_number) - 1): y + 1])
                # for l in sub_matrix:
                #     print(l)
                for row in sub_matrix:
                    for v in row:
                        if not v.isdigit() and v != ".":
                            new_total += int(curr_number)
                            logger.info(curr_number)
                curr_number = ""

logger.info(new_total)

logger.info("PARTE 2")


def iterate_cross_position(matrix, x, y):
    tmp_list = []
    tmp_list.append(matrix[x][y + 1])
    tmp_list.append(matrix[x][y - 1])
    tmp_list.append(matrix[x + 1][y + 1])
    tmp_list.append(matrix[x + 1][y - 1])
    tmp_list.append(matrix[x + 1][y])
    tmp_list.append(matrix[x - 1][y + 1])
    tmp_list.append(matrix[x - 1][y - 1])
    tmp_list.append(matrix[x - 1][y])
    tmp_list = [val for val in tmp_list if val != "."]
    return len(tmp_list) >= 2

def most_near(start, end, y):
    if start is None:
        return end
    if end is None:
        return start
    return start if abs(y - start) < abs(y - end) else end


def extract_number(matrix, x, y):
    sub_matrix = []
    total_number = []
    sub_matrix.append(matrix[x - 1])
    sub_matrix.append(matrix[x])
    sub_matrix.append(matrix[x + 1])
    for q in range(3):
        numb = ""
        start_index = None
        end_index = None
        for i in range(len(sub_matrix[q])):
            if str(sub_matrix[q][i]).isdigit():
                if numb == "":
                    start_index = i
                else:
                    end_index = i
                numb += sub_matrix[q][i]
            elif start_index is not None or end_index is not None:
                most_near_number = most_near(start_index,end_index,y)
                if start_index == y or end_index == y:
                    total_number.append(int(numb))
                    numb = ""
                    start_index = None
                    end_index = None
                elif abs(most_near_number -y) <=1:
                    total_number.append(int(numb))
                    numb = ""
                    start_index = None
                    end_index = None
                else:
                    numb = ""
                    start_index = None
                    end_index = None
    return total_number


matrix = []
with open("input.txt") as f:
    for line in f:
        matrix.append(list(line.replace("\n", "")))

for l in matrix:
    print(l)

c = len(matrix[0])
r = len(matrix)

print("#######")

tmp = ["." for _ in range(c)]
matrix.insert(0, tmp)
matrix.insert(c + 1, tmp)

for i in range(c + 1):
    matrix[i].insert(0, ".")
    matrix[i].insert(c + 1, ".")

print("#######")
for l in matrix:
    print(l)

curr_number = ""

c = len(matrix[0])
r = len(matrix)
new_total = 0

for x in range(c):
    for y in range(r):
        if (matrix[x][y] == "*"):
            # Guardo quanti numeri ho a fianco
            if not iterate_cross_position(matrix, x, y):
                logger.info(f"SKIP {x} {y}")
                continue
            else:
                tmp_numbers = extract_number(matrix, x, y)
                if len(tmp_numbers)==2:
                    vv = reduce(lambda x, y: x * y, tmp_numbers, 1)
                    new_total += vv

print(new_total)