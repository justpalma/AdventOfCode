from loguru import logger


def get_card_number(line):
    return line.split(":")[0].split(" ")[-1]


def get_numbers(line):
    tmp = line.split(":")[1].split("|")
    winning = []
    my = []
    tmp[0] = tmp[0].replace("\n", "")
    tmp[1] = tmp[1].replace("\n", "")
    logger.info(tmp)
    for x in tmp[0].split(" "):
        if x.isnumeric():
            winning.append(int(x))

    for x in tmp[1].split(" "):
        if x.isnumeric():
            my.append(int(x))

    return winning, my


def get_matching_number(winning, my):
    total = 0
    for x in winning:
        if x in my:
            total += 1
    return total


total_point = 0
with open("input.txt") as f:
    for line in f:
        total_match = 0
        current_point = 1
        winning, my = get_numbers(line)
        logger.info(f"{winning}  -  {my}")
        for elem in winning:
            if elem in my:
                total_match += 1
        logger.info(f"Total match {total_match}")
        if total_match != 0:
            if total_match == 1:
                total_point += 1
            else:
                total_match -= 1
                for _ in range(total_match):
                    current_point *= 2
                total_point += current_point
        logger.info(f"{current_point}")

    logger.info(total_point)

logger.info("PARTE 2")

# data_structure = [
#     {
#         "id": int,
#         "winning": [],
#         "my": [],
#         "original": int,
#         "copy": int
#     }
# ]
data_structure = []
with open("input.txt") as f:
    for line in f:
        id = get_card_number(line)
        winning, my = get_numbers(line)
        data_structure.append(
            {
                "id": int(id),
                "winning": winning,
                "my": my,
                "original": 1,
                "copy": 0
            }
        )

for index, elem in enumerate(data_structure):
    id = elem['id']
    matching_number = get_matching_number(elem['winning'], elem['my'])
    logger.info(f"id {id} fa match con {matching_number}")
    to_add = elem['original'] + elem['copy']
    for x in range(id+1, id + matching_number +1 ):
        logger.info(f"Aggiungo Carta {x} con indice {x-1}, ovvero {data_structure[x-1]}")
        data_structure[x-1]['copy'] += to_add

total = 0

for x in data_structure:
    total += x['original'] + x['copy']

logger.info(total)
