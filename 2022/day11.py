import itertools
from math import prod

raw = open('input/day11.txt', 'r')
# raw = open('input/test.txt', 'r')
raw_monkeys = [ x.strip() for x in raw.read().split("Monkey")][1:]
monkeys = []

class Monkey(object):
    number = -1
    items = None
    operation = ""
    test_value = -1
    inspections = -1
    true_target = -1
    false_target = -1
    relief = 3


    def __init__(self, raw):
        lines = [line.strip() for line in raw.splitlines()]
        self.number = lines[0].rstrip(":")
        self.inspections = 0
        self.items = [int(x) for x in lines[1].lstrip("Starting items: ").split(",")]
        self.operation = lines[2].split(" = ")[1]
        self.test_value = int(lines[3].lstrip("Test: divisible by "))
        self.true_target = int(lines[4].lstrip("If true: throw to monkey "))
        self.false_target = int(lines[5].lstrip("If false: throw to monkey "))

    def inspect_items(self):
        for item in self.items:
            self.inspect_item(item)
        self.items = []
    
    def inspect_item(self,item):
        self.inspections += 1
        item = eval(self.operation, {}, {"old": item})
        if self.relief == 3:
            item = item // self.relief
        else:
            item = item % self.relief
        if item % self.test_value == 0:
            monkeys[self.true_target].catch(item)
        else:
            monkeys[self.false_target].catch(item)

    def catch(self, item):
        self.items.append(item)

    def __str__(self):
        return dedent(f"""
                    Monkey {self.number}:
                        Items: {", ".join(map(str,self.items))}
                        Operation: new = {self.operation}
                        Test: divisible by {self.test_value}
                            If true: throw to monkey {self.true_target}
                            If false: throw to monkey {self.false_target}
                    """).strip("\n")
    

for raw_monkey in raw_monkeys:
    monkeys.append(Monkey(raw_monkey))

rounds = 20

for _ in range(rounds):
    for monkey in monkeys:
        monkey.inspect_items()

for monkey in monkeys:
    print(f"Monkey {monkey.number} inspected items {monkey.inspections} times.")

print()
inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
p1 = inspections[0]*inspections[1]

print(f"part 1: {p1}")


monkeys = []
for raw_monkey in raw_monkeys:
    monkeys.append(Monkey(raw_monkey))

relief = prod([monkey.test_value for monkey in monkeys])

for monkey in monkeys:
    monkey.relief = relief
rounds = 10000

for i in range(rounds):
    for monkey in monkeys:
        monkey.inspect_items()

for monkey in monkeys:
    print(f"Monkey {monkey.number} inspected items {monkey.inspections} times.")

print()
inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
p2 = inspections[0]*inspections[1]

print(f"part 2: {p2}")