data_time = []
data_distance = []
with open("input.txt") as f:
    data_time = f.readline()
    data_distance = f.readline()

data_time = [int(x) for x in data_time.replace("\n", "").split(":")[1].split(" ") if x != ""]
data_distance = [int(x) for x in data_distance.replace("\n", "").split(":")[1].split(" ") if x != ""]
total = 1
for index, t in enumerate(data_time):
    winning = 0
    for t_step in range(t):
        final_pos = t_step * (t - t_step)
        if (final_pos > data_distance[index]):
            print(f"with {t} and pressed {t_step} i won final pos is {final_pos} and record is {data_distance[index]}")
            winning += 1
    total *= winning

print(total)

print("parte 2")
with open("input.txt") as f:
    data_time = f.readline()
    data_distance = f.readline()

data_time = [x for x in data_time.replace("\n", "").split(":")[1].split(" ") if x != ""]
data_distance = [x for x in data_distance.replace("\n", "").split(":")[1].split(" ") if x != ""]

data_time = int("".join([x for x in data_time]))
data_distance = int("".join([x for x in data_distance]))

print(data_time)
print(data_distance)

winning = 0
for t_step in range(data_time):
    final_pos = t_step * (data_time - t_step)
    if (final_pos > data_distance):
        #print(f"with {data_time} and pressed {t_step} i won final pos is {final_pos} and record is {data_distance}")
        winning += 1

print(winning)