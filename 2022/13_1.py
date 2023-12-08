filename = 'resources/day_13_input.txt'
#filename = 'resources/debug.txt'


def analyze_pair(l1, l2):
    for subl1, subl2 in zip(l1, l2):
        if isinstance(subl1, int)  and isinstance(subl2, int):
            if subl1 == subl2: continue
            return subl2 - subl1
        elif isinstance(subl1, list) and isinstance(subl2, int):
            subl2 = [subl2]
            c = analyze_pair(subl1, subl2)
            if c == 0:
                continue
            else:
                return c
        elif isinstance(subl2, list) and isinstance(subl1, int):
            subl1 = [subl1]
            c = analyze_pair(subl1, subl2)
            if c == 0:
                continue
            else:
                return c
        elif isinstance(subl1, list) and isinstance(subl2, list):
            c = analyze_pair(subl1, subl2)
            if c == 0:
                continue
            else:
                return c
    if len(l1) < len(l2):
        return 1
    elif len(l2) < len(l1):
        return -1
    return 0



# def resolve():
#     data = load_input()
#     tot_iter = len(data) / 2
#     count = 0
#     res = []
#     msg = 0
#     while count < tot_iter:
#         count += 1
#         l1 = convert_line(data[msg])
#         msg += 1
#         l2 = convert_line(data[msg])
#         msg += 1
#         if analyze_pair(l1, l2):
#             res.append(count)
#     print(res)
#     print(sum(res))

with open(filename) as file:
    x = [[eval(b) for b in a.strip().split('\n')] for a in file.read().split('\n\n')]

total_right = 0
for i,l in enumerate(x):
    right = analyze_pair(l[0], l[1])
    if right > 0: total_right += i+1
print(total_right)