from typing import Iterable, Tuple, TypeVar

T = TypeVar("T")
from loguru import logger


def get_seeds(line):
    tmp = line.split(":")[1].split(" ")
    return [int(x) for x in tmp if x != ""]


def extract_couples_map(line):
    return line.split(" ")[0].split("-")[0], line.split(" ")[0].split("-")[2]


def extract_map(line):
    return line.split(" ")[0].replace(" ", "")


def get_values(line):
    tmp = line.split(" ")
    return int(tmp[0]), int(tmp[1]), int(tmp[2])


def grouped(iterable: Iterable[T], n=2) -> Iterable[Tuple[T, ...]]:
    """s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), ..."""
    return zip(*[iter(iterable)] * n)


def get_seeds_range(line):
    tmp = list(line.split(": ")[1].split(" "))
    logger.info(tmp)
    tmp = sorted([int(x) for x in tmp])
    tmp_list = [(int(x), int(y)) for x,y in grouped(tmp, n=2)]
    return tmp_list


data_structure = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}

with open("input.txt") as f:
    for index, line in enumerate(f):
        line = line.replace("\n", "")
        if index == 0:
            seeds = get_seeds(line)
            continue
        if not len(line) == 0:
            if not str(line[0]).isdigit():
                curr_map = extract_map(line)
            else:
                dst, src, lgt = get_values(line)
                data_structure[curr_map].append({
                    "dst": dst,
                    "src": src,
                    "lgt": lgt,
                })

logger.info(data_structure)

logger.info(seeds)

result = []

for s in seeds:
    soil = s
    for v in data_structure['seed-to-soil']:
        if not (v['src'] <= s < (v['src'] + v['lgt'])):
            continue
        soil = v['dst'] + (s - v['src'])
    fert = soil
    for v in data_structure['soil-to-fertilizer']:
        if not (v['src'] <= soil < (v['src'] + v['lgt'])):
            continue
        fert = v['dst'] + (soil - v['src'])
    water = fert
    for v in data_structure['fertilizer-to-water']:
        if not (v['src'] <= fert < (v['src'] + v['lgt'])):
            continue
        water = v['dst'] + (fert - v['src'])

    light = water
    for v in data_structure['water-to-light']:
        if not (v['src'] <= water < (v['src'] + v['lgt'])):
            continue
        light = v['dst'] + (water - v['src'])

    temp = light
    for v in data_structure['light-to-temperature']:
        if not (v['src'] <= light < (v['src'] + v['lgt'])):
            continue
        temp = v['dst'] + (light - v['src'])

    hum = temp
    for v in data_structure['temperature-to-humidity']:
        if not (v['src'] <= temp < (v['src'] + v['lgt'])):
            continue
        hum = v['dst'] + (temp - v['src'])

    loc = hum
    for v in data_structure['humidity-to-location']:
        if not (v['src'] <= hum < (v['src'] + v['lgt'])):
            continue
        loc = v['dst'] + (hum - v['src'])

    logger.info(f"{s}  {soil}  {fert}  {water}  {light}  {temp}  {hum}  {loc}")
    result.append(loc)

logger.info(min(result))




# data_structure = {
#     "seed-to-soil": [],
#     "soil-to-fertilizer": [],
#     "fertilizer-to-water": [],
#     "water-to-light": [],
#     "light-to-temperature": [],
#     "temperature-to-humidity": [],
#     "humidity-to-location": [],
# }
# with open("input.txt") as f:
#     for index, line in enumerate(f):
#         line = line.replace("\n", "")
#         if index == 0:
#             seeds = get_seeds_range(line)
#             continue
#         if not len(line) == 0:
#             if not str(line[0]).isdigit():
#                 curr_map = extract_map(line)
#             else:
#                 dst, src, lgt = get_values(line)
#                 data_structure[curr_map].append({
#                     "dst": dst,
#                     "src": src,
#                     "lgt": lgt,
#                 })
#
# logger.info(data_structure)
#
# logger.info(seeds)
#
# result = set()
#
# min_value = None
#
# for s in seeds:
#     # logger.info(s)
#     start = s[0]
#     stop = start + s[1]
#     logger.info(f"{start} {stop}")
#     while start <= stop:
#         print(start)
#         soil = start
#         # logger.info("sts")
#         for v in data_structure['seed-to-soil']:
#             if not (v['src'] <= start < (v['src'] + v['lgt'])):
#                 continue
#             soil = v['dst'] + (start - v['src'])
#         fert = soil
#         # logger.info("stf")
#         for v in data_structure['soil-to-fertilizer']:
#             if not (v['src'] <= soil < (v['src'] + v['lgt'])):
#                 continue
#             fert = v['dst'] + (soil - v['src'])
#         water = fert
#         # logger.info("ftw")
#         for v in data_structure['fertilizer-to-water']:
#             if not (v['src'] <= fert < (v['src'] + v['lgt'])):
#                 continue
#             water = v['dst'] + (fert - v['src'])
#
#         light = water
#         # logger.info("wtl")
#         for v in data_structure['water-to-light']:
#             if not (v['src'] <= water < (v['src'] + v['lgt'])):
#                 continue
#             light = v['dst'] + (water - v['src'])
#
#         temp = light
#         # logger.info("ltt")
#         for v in data_structure['light-to-temperature']:
#             if not (v['src'] <= light < (v['src'] + v['lgt'])):
#                 continue
#             temp = v['dst'] + (light - v['src'])
#
#         hum = temp
#         # logger.info("tth")
#         for v in data_structure['temperature-to-humidity']:
#             if not (v['src'] <= temp < (v['src'] + v['lgt'])):
#                 continue
#             hum = v['dst'] + (temp - v['src'])
#
#         loc = hum
#         # logger.info("htl")
#         for v in data_structure['humidity-to-location']:
#             if not (v['src'] <= hum < (v['src'] + v['lgt'])):
#                 continue
#             loc = v['dst'] + (hum - v['src'])
#
#         # logger.info(f"{s}  {soil}  {fert}  {water}  {light}  {temp}  {hum}  {loc}")
#         if min_value is None:
#             min_value = loc
#         elif loc < min_value:
#             min_value = loc
#         #result.add(loc)
#         start += 1
#
# # logger.info(min(result))
# logger.info(min_value)