win = 6
draw = 3
lose = 0

my_point = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
# false perdo
# true vinco
# 0 pareggio
cases = {
    'AX': -1,
    'AY': True,
    'AZ': False,
    'BX': False,
    'BY': -1,
    'BZ': True,
    'CX': True,
    'CY': False,
    'CZ': -1,
}


def find_winner(elf, me):
    print(elf,me)
    current = my_point.get(me)
    if cases.get(elf + me) == -1:
        print("PARI")
        return draw + current
    elif cases.get(elf + me):
        print("W")
        return win + current
    else:
        print("L")
        return lose + current


with open("resources/day_2_input.txt") as file:
    point = 0
    for line in file:
        l = line.rstrip()
        point += find_winner(l.split(' ')[0], l.split(' ')[1])
    print(point)