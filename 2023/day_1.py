
first_c = ""
last_c = ""
total = 0

# PART 1
# with open("input.txt") as f:
#     for line in f:
#         for c in line:
#             if c.isdigit():
#                 first_c = c
#                 break
#         for c in reversed(line):
#             if c.isdigit():
#                 last_c = c
#                 break
#         total += int(first_c+last_c)



# PART 2
def get_index_of_element(line, reverse=False):
    nums = {
        "one": None,
        "two": None,
        "three": None,
        "four": None,
        "five": None,
        "six": None,
        "seven": None,
        "eight": None,
        "nine": None,
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "7": None,
        "8": None,
        "9": None
    }

    rvs_nums = {
        "eno": None,
        "owt": None,
        "eerht": None,
        "ruof": None,
        "evif": None,
        "xis": None,
        "neves": None,
        "thgie": None,
        "enin": None,
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "7": None,
        "8": None,
        "9": None
    }

    tmp_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    if reverse:
        for k in rvs_nums.keys():
            try:
                rvs_nums[k] = line.index(k)
            except ValueError:
                rvs_nums[k] = None
        filtered_dict = {key: value for key, value in rvs_nums.items() if value is not None}
        min_key = min(filtered_dict, key=filtered_dict.get)
        if min_key.isdigit():
            return min_key
        else:
            return tmp_nums[min_key[::-1]]
    else:
        for k in nums.keys():
            try:
                nums[k] = line.index(k)
            except ValueError:
                nums[k] = None
        filtered_dict = {key: value for key, value in nums.items() if value is not None}
        min_key = min(filtered_dict, key=filtered_dict.get)
        if min_key.isdigit():
            return min_key
        else:
            return tmp_nums[min_key]

    # print(nums)
    # print(rvs_nums)
    # if reverse:
    #     filtered_dict = {key: value for key, value in rvs_nums.items() if value is not None}
    # else:
    #     filtered_dict = {key: value for key, value in nums.items() if value is not None}
    # # Find the key with the minimum value
    # min_key = min(filtered_dict, key=filtered_dict.get)
    #
    # if min_key.isdigit():
    #     return min_key
    # else:
    #     return tmp_nums[min_key]





with open("input.txt") as f:
    for line in f:
        first_c=str(get_index_of_element(line))
        last_c=str(get_index_of_element(line[::-1], True))
        print(first_c+last_c)
        total += int(first_c + last_c)
    print(total)