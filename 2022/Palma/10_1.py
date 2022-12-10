filename = "resources/day_10_input.txt"

cicle = [20, 60, 100, 140, 180, 220]


def check_cicle(c):
    if c in cicle:
        return True


def resolve():
    strength = 0
    total_strength = 0
    x = 1
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            command = line.split(' ')[0]
            if command == 'addx':
                inc = int(line.split(' ')[1])
                for sub in range(2):
                    strength += 1
                    if check_cicle(strength):
                        print(f'f {strength}, x {x}')
                        total_strength += strength * x
                    if sub == 1:
                        x += inc
            else:
                strength += 1
                if check_cicle(strength):
                    print(f'f {strength}, x {x}')
                    total_strength += strength * x
            print(x)


    print(total_strength)


resolve()
