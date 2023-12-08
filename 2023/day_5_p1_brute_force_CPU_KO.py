from loguru import logger


def get_seeds(line):
    tmp = line.split(":")[1].split(" ")
    return [int(x) for x in tmp if x != ""]


def extract_couples_map(line):
    return line.split(" ")[0].split("-")[0], line.split(" ")[0].split("-")[2]


def get_values(line):
    tmp = line.split(" ")
    return int(tmp[0]), int(tmp[1]), int(tmp[2])


def calculate_ranges(dst, src, lgt):
    data = []
    for x in range(lgt):
        data.append((src + x, dst + x))
    return data


data_structure = {}

with open("input.txt") as f:
    left_elem = ""
    right_elem = ""
    for index, line in enumerate(f):
        line = line.replace("\n", "")
        if index == 0:
            seeds = get_seeds(line)
            continue
        if not len(line) == 0:
            if not str(line[0]).isdigit():
                left_elem, right_elem = extract_couples_map(line)
                data_structure[left_elem] = {}
            else:
                dst, src, lgt = get_values(line)
                data = calculate_ranges(dst, src, lgt)
                for x in data:
                    data_structure[left_elem][x[0]] = x[1]
                pass

logger.info("FINITO PARSING FILE")

dt_soil = data_structure['seed']
dt_fertilizer = data_structure['soil']
dt_water = data_structure['fertilizer']
dt_light = data_structure['water']
dt_temperature = data_structure['light']
dt_humidity = data_structure['temperature']
dt_location = data_structure['humidity']

dt_seed = {
        s: {
            "seed": s
    } for s in seeds}

for s in seeds:
    soil = dt_soil.get(s, s)
    fertilizer = dt_fertilizer.get(soil, soil)
    water = dt_water.get(fertilizer, fertilizer)
    light = dt_light.get(water, water)
    temperature = dt_temperature.get(light, light)
    humidity = dt_humidity.get(temperature, temperature)
    location = dt_location.get(humidity, humidity)
    dt_seed[s]["location"] = location

lowest = None

for k,v in dt_seed.items():
    if lowest is None:
        lowest = v['location']
    elif  v['location'] < lowest:
        lowest = v['location']


logger.info(lowest)
