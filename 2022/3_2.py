import string


def get_value(val):
    return mapping.index(val) + 1


mapping = list(string.ascii_lowercase + string.ascii_uppercase)

with open("resources/day_3_input.txt") as file:
    point = 0
    while True:
        set1 = set()
        result = set()
        l1 = set(file.readline().rstrip())
        if len(l1) == 0:
            break
        l2 = set(file.readline().rstrip())
        l3 = set(file.readline().rstrip())

        point += get_value(l1.intersection(l2).intersection(l3).pop())

print(point)
