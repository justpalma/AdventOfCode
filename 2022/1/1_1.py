
max = 0
current = 0


with open("input.txt") as file:
    for line in file:
        l = line.rstrip()
        if line == '\n':
            if current > max:
                max = current
            current = 0
        else:
            line = line.strip()
            c = int(line)
            current += c

    if current > max:
        max = current

print(max)


