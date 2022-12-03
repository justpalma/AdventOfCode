max = [0,0,0]
current = 0

with open("resources/day_1_input.txt") as file:
    for line in file:
        l = line.rstrip()
        if line == '\n':
            if current > max[2]:
                max[2] = current
                max.sort(reverse = True)
            current = 0
        else:
            line = line.strip()
            c = int(line)
            current += c

    if current > max[2]:
        max[2] = current
        max.sort(reverse=True)

print(max)

print(sum(max))
