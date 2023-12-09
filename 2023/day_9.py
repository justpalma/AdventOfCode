from pprint import pprint


def calculate_difference(line, pos):
    last_val = 0
    new_line = []
    for index, x in enumerate(line):
        if index == len(line) - 1:
            break
        new_line.append(line[index + 1] - x)
    #print(f"{new_line} - - - - - {len(new_line)}")
    return new_line, new_line[pos]


def is_all_zero(line: list):
    return line.count(0) == len(line)


def resolve_p1():
    lines = []
    total = 0
    with open("input.txt") as f:
        for x in f:
            lines.append([int(x) for x in x.replace("\n", "").split(" ")])

    for index, line in enumerate(lines):
        last_vals_list = []
        tmp_val = lines[index]
        last_vals_list.append(tmp_val[-1])
        print(f"{tmp_val} - - - - - {len(tmp_val)}")
        while True:
            tmp_val, last_val = calculate_difference(tmp_val, -1)
            last_vals_list.insert(0, last_val)
            if is_all_zero(tmp_val):
                break

        total += sum(last_vals_list)

    print(total)




def resolve_p2():
    lines = []
    total = 0
    with open("input.txt") as f:
        for x in f:
            lines.append([int(x) for x in x.replace("\n", "").split(" ")])

    for index, line in enumerate(lines):
        last_vals_list = []
        tmp_val = lines[index]
        last_vals_list.append(tmp_val[0])
        #print(f"{tmp_val} - - - - - {len(tmp_val)}")
        while True:
            tmp_val, last_val = calculate_difference(tmp_val, 0)
            last_vals_list.insert(0, last_val)
            if is_all_zero(tmp_val):
                break
        tmp_total = last_vals_list[0]
        for index, q in enumerate(last_vals_list):
            if index == len(last_vals_list) - 1:
                break
            tmp_total = -1 *(tmp_total - last_vals_list[index+1])
        total += tmp_total

    print(total)
