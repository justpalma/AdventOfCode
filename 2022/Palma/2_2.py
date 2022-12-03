win = 6
draw = 3
lose = 0

my_point = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
# Y pareggio
# X perdo
# Z vinco
cases = {
    'AX': False,
    'AY': -1,
    'AZ': True,
    'BX': False,
    'BY': -1,
    'BZ': True,
    'CX': False,
    'CY': -1,
    'CZ': True,
}

def get_my_point(elf, end):
    if end == -1:
        if elf == 'A':
            return my_point.get('X')
        if elf == 'B':
            return my_point.get('Y')
        if elf == 'C':
            return my_point.get('Z')
    if end:
        if elf == 'A':
            return my_point.get('Y')
        if elf == 'B':
            return my_point.get('Z')
        if elf == 'C':
            return my_point.get('X')
    if not end:
        if elf == 'A':
            return my_point.get('Z')
        if elf == 'B':
            return my_point.get('X')
        if elf == 'C':
            return my_point.get('Y')



def find_winner(elf, me):
    print(elf,me)
    current = get_my_point(elf, cases.get(elf + me))
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