import math

filename = 'resources/day_11_input.txt'
#filename = 'resources/debug.txt'


class Monkey(object):
    def __init__(self, raw_data: list[str]):
        self._raw_data = raw_data
        self._id = 0
        self._items = []
        self._op_symbol = ''
        self._op_value = ''
        self._test_value = 0
        self._true_cond = 0
        self._false_cond = 0
        self.__populate_monkey()
        self._inspections = 0

    def __populate_monkey(self):
        self._id = int(self._raw_data[0].replace(':', '').split(' ')[1])
        self._items = [int(n) for n in
                       self._raw_data[1].replace('Starting items:', '').replace(',', '').lstrip().rstrip().split(' ')]
        self._op_symbol = self._raw_data[2].replace(':', '').split(' ')[4]
        self._op_value = self._raw_data[2].replace(':', '').split(' ')[5]
        self._test_value = int(self._raw_data[3].replace(':', '').split(' ')[3])
        self._true_cond = int(self._raw_data[4].replace(':', '').split(' ')[5])
        self._false_cond = int(self._raw_data[5].replace(':', '').split(' ')[5])

    @property
    def id(self):
        return self._id

    @property
    def op_symbol(self):
        return self._op_symbol

    @property
    def op_value(self):
        return self._op_value

    @property
    def test_value(self):
        return self._test_value

    @property
    def true_cond(self):
        return self._true_cond

    @property
    def false_cond(self):
        return self._false_cond

    @property
    def items(self):
        return self._items

    @property
    def inspections(self):
        return self._inspections

    def calculate_worry_level(self, val):
        second_term = val if self.op_value == 'old' else int(self.op_value)
        if self.op_symbol == '+':
            return val + second_term
        if self.op_symbol == '*':
            return val * second_term

    def perform_test(self, worry):
        dst = self._false_cond
        worry = math.floor(worry / 3)
        if worry % self.test_value == 0:
            dst = self._true_cond
        return [dst, worry]

    def play(self, index):
        self._inspections += 1
        val = self.items[index]
        val = self.calculate_worry_level(val)
        return self.perform_test(val)

    def clear_items(self):
        self._items = []

    def __str__(self):
        return f'id: {self.id} ' \
               f'items: {self.items} ' \
               f'opeartion: {self.op_symbol}{self.op_value} ' \
               f'test: {self.test_value} ' \
               f'true_cond: {self.true_cond} ' \
               f'false_cond: {self.false_cond}'


def clean_data(data: list[str]):
    new_data = []
    for x in range(len(data)):
        tmp = data[x].rstrip().lstrip()
        if tmp:
            new_data.append(tmp)
    return new_data


def load_monkey():
    monkey = []
    with open(filename) as file:
        data = file.readlines()
    data = clean_data(data)
    total_monkey = get_total_monkey(data)
    for m in range(total_monkey):
        i = m * 6
        monkey.append(Monkey(data[i:i + 6]))

    return monkey


def get_total_monkey(data):
    tot = 0
    for x in data:
        if 'Monkey' in x:
            tot += 1
    return tot


def resolve():
    total_monkey = load_monkey()
    total_inspected = []

    for _ in range(20):
        for m in total_monkey:
            perform_op = []
            for index, item in enumerate(m.items):
                result = m.play(index)
                print(f'spedico {result[1]} a {result[0]}')
                perform_op.append(result)
            m.clear_items()
            for op in perform_op:
                total_monkey[op[0]].items.append(op[1])

    for m in total_monkey:
        print(m.inspections)
        total_inspected.append(m.inspections)

    print(total_inspected)

    total_inspected = sorted(total_inspected, reverse=True)
    return total_inspected[0]*total_inspected[1]

print(resolve())

