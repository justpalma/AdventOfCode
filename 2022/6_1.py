filename = "resources/day_6_input.txt"

l = ['a', 'b', 'a', 'd']
print(set(l))

def is_set(l):
    s = set(l)
    if len(s) == 4:
        return True
    return False

def get_index():
    l = []
    index = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            for c in line:
                l.append(c)
                index += 1
                if len(l) == 4:
                    if not is_set(l):
                        l.pop(0)
                    else:
                        return index


print(get_index())

