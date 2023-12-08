import math
from pprint import pprint


def convert_line(line):
    return line.split(" = ")[0], (line.split(" = ")[1].replace("(", "").replace(")", "")).split(", ")



def step_to_finish(data_structure, instruction, start):
    step = 0
    curr_index = 0
    key = start
    max_elem = len(instruction) - 1
    while True:
        if instruction[curr_index] == "L":
            key = data_structure[key][0]
        if instruction[curr_index] == "R":
            key = data_structure[key][1]
        step += 1
        if str(key).endswith("Z"):
            return step
        curr_index += 1
        if curr_index > max_elem:
            curr_index = 0






def resolve_p1():
    with open('input.txt', 'r') as f:
        lines = list(map(str.strip, f))

    print(lines)

    for index, x in enumerate(lines):
        if x == "":
            del lines[index]

    print(lines)

    instruction = lines[0]
    del lines[0]

    print(instruction)
    data_structure = {}
    for x in lines:
        node, tmp_instr = convert_line(x)
        data_structure[node] = tmp_instr

    pprint(data_structure)
    print(step_to_finish(data_structure, instruction, "AAA"))
    # max_elem = len(instruction) - 1
    # curr_index = 0
    # next_step = ""
    # step = 0
    # key = "AAA"
    # while True:
    #     if instruction[curr_index] == "L":
    #         key = data_structure[key][0]
    #     if instruction[curr_index] == "R":
    #         key = data_structure[key][1]
    #     step += 1
    #     if key == "ZZZ":
    #         print(f"FINISH {step}")
    #         break
    #     curr_index += 1
    #     if curr_index > max_elem:
    #         curr_index = 0


def get_starting_nodes(dt):
   return [k for k in dt.keys() if k[-1] == "A"]

def all_nodes_ends_with_z(nodes):
    for x in nodes:
        if x[-1] != "Z":
            return False
        print(f"{x} end with Z, {nodes}")
    return True


def resolve_p2():
    with open('input.txt', 'r') as f:
        lines = list(map(str.strip, f))

    print(lines)

    for index, x in enumerate(lines):
        if x == "":
            del lines[index]

    print(lines)

    instruction = lines[0]
    del lines[0]

    print(instruction)
    data_structure = {}
    for x in lines:
        node, tmp_instr = convert_line(x)
        data_structure[node] = tmp_instr

    pprint(data_structure)
    current_nodes = get_starting_nodes(data_structure)
    res = []
    for x in current_nodes:
        res.append(step_to_finish(data_structure, instruction, x))

    print(math.lcm(*res))

