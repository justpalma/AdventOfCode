filename = "resources/day_5_input.txt"
#filename = "resources/input2.txt"


def get_total_crates():
    with open(filename) as file:
        for line in file:
            return len(line) // 4


def load_stacks():
    crates = [[] for _ in range(get_total_crates())]
    with open(filename) as file:
        for line in file:
            index = 0
            if line == '\n':
                return crates
            line = line.rstrip()
            while index <= len(line):
                current_stack = line[index:index + 3]
                if '[' in current_stack:
                    elem = current_stack[1]
                    crates[index//4].append(elem)
                index += 4

def perform_move(crates):
    with open(filename) as file:
        for line in file:
            if 'move' not in line:
                continue
            else:
                movement = line.split(' ')
                total_mov = int(movement[1])
                src = int(movement[3])
                dst = int(movement[5])
                for m in range(total_mov):
                    elem_to_move = crates[src-1].pop(0)
                    crates[dst - 1].insert(0, elem_to_move)
                    print(f"Move {elem_to_move} from {src} to {dst}")
    return crates



result = perform_move(load_stacks())

for x in result:
    print(x[0], end='')


