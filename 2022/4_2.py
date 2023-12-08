

def overlaps(interval_1, interval_2):
    s1 = set(x for x in range(int(interval_1.split("-")[0]), int(interval_1.split("-")[1]) +1))
    s2 = set(x for x in range(int(interval_2.split("-")[0]), int(interval_2.split("-")[1]) +1))
    if len(s1.intersection(s2)) > 0:
       return 1
    return 0



with open("resources/day_4_input.txt") as file:
    point = 0
    for line in file:
        line = line.split(',')
        point+=overlaps(line[0], line[1])

    print(point)