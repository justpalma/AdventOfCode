from collections import defaultdict
filename = "resources/day_7_input.txt"
#filename = "resources/debug.txt"

MAX_SIZE = 70000000
REQUIRED = 30000000
CD_BACK = -1
CD_IN = 1


def is_command(l):
    return True if l[0] == '$' else False


def is_dir(l):
    return True if 'dir ' in l else False


def get_folder_name(l):
    if is_command(l):
        return l.split(' ')[2]
    return l.split(' ')[1]


def get_file_size(l):
    return l.split(' ')[0]


def get_file_name(l):
    return l.split(' ')[1]


def which_command(l):
    """
    -1: cd ..
    0: ls
    1: cd in folder
    """
    if '$ cd' not in l or '/' in l:
        return 0
    elif '$ cd ..' in l:
        return CD_BACK
    else:
        return CD_IN


def get_total():
    dir_order = ['/']
    files = {}
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if is_command(line):
                cmd = which_command(line)
                if cmd == CD_BACK:
                    dir_order.pop()
                elif cmd == CD_IN:
                    dir = get_folder_name(line)
                    dir_order.append(dir)
            elif not is_dir(line):
                file_name = get_file_name(line)
                file_size = get_file_size(line)
                files[tuple(dir_order) + (file_name,)] = int(file_size)

    total = defaultdict(int)
    for path, size in files.items():
        pwd = []
        for folder in path:
            total[tuple(pwd)] += size
            pwd.append(folder)

    root_folder_size = total[tuple('/')]
    return root_folder_size, [size for size in total.values()]


def find_smallest_to_delete(used, folder):
    minimun = 10000000000000
    for elem in folder:
        free_after_delete = MAX_SIZE - (used - elem)
        if free_after_delete >= REQUIRED:
            if elem <= minimun:
                minimun = elem
    return minimun

print(get_total())
used, folders = get_total()
print(find_smallest_to_delete(used,folders))
