import string

def get_value(val):
    return mapping.index(val) + 1


mapping = list(string.ascii_lowercase + string.ascii_uppercase)

with open("resources/day_3_input.txt") as file:
    point = 0
    for line in file:
        l = len(line) // 2
        first_half = set(line[:l])
        second_half = set(line[l:])
        point += get_value(first_half.intersection(second_half).pop())

print(point)
