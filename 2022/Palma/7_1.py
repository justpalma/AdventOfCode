from collections import defaultdict
filename = "resources/day_7_input.txt"


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

    return sum([size for size in total.values() if size <= 100000])


print(get_total())
