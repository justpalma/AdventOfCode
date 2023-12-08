def get_game_ID(line):
    return line.split(":")[0].split(" ")[1], line.split(":")[1]


def get_game_sets(line):
    return line.split(";")


def get_game_number_by_color(line, color):
    line = line.replace(",", " ")
    line = line.replace("\n", " ")
    elements = line.split(' ')
    elements = [i for i in elements if i != ""]
    try:
        return elements[elements.index(color) - 1]
    except Exception:
        return False


def is_valid(amount, color):
    match color:
        case "red":
            return int(amount) <= 12
        case "blue":
            return int(amount) <= 14
        case "green":
            return int(amount) <= 13
        case _:
            raise Exception("ERRORE")


def is_valid_game(line):
    line = line.replace(",", " ")
    line = line.replace("\n", " ")
    elements = line.split(' ')
    elements = [i for i in elements if i != ""]

    for x in elements:
        if str(x).isdigit():
            color = elements[elements.index(x) + 1]
            tmp = is_valid(x, color)
            if not tmp:
                return False
            else:
                del elements[elements.index(x)]
    return True






with open("input.txt") as f:
    colors = ["red", "green", "blue"]
    total = 0
    for line in f:
        valid = True
        game_id, line = get_game_ID(line)
        game_sets = get_game_sets(line)
        for games in game_sets:
            if not is_valid_game(games):
                valid = False
                break
        if valid:
            print(f"{game_id} is valid")
            total += int(game_id)



print("PARTE 2#####")
# Parte 2
with open("input.txt") as f:
    colors = ["red", "green", "blue"]
    full_total = 0
    for line in f:
        total = 1
        tmp_data = {
            "red": False,
            "green": False,
            "blue": False
        }
        valid = True
        game_id, line = get_game_ID(line)
        game_sets = get_game_sets(line)
        for games in game_sets:
            for c in colors:
                tmp = get_game_number_by_color(games, c)
                if tmp:
                    if not tmp_data[c] or tmp_data[c] < int(tmp):
                        tmp_data[c] = int(tmp)
        for k,v in tmp_data.items():
            total *= int(v)
        full_total += total

    print(full_total)