import itertools
from functools import cmp_to_key
from math import prod
raw = open('input/day13.txt', 'r')
DEBUG=False
# raw = open('input/test.txt', 'r')
# DEBUG=True
f = [ x.strip().splitlines() for x in raw.read().split("\n\n")]

def debug(msg=""):
    if DEBUG:
        print(msg)

def compare(left, right, depth=0):
    prefix = "  "*depth
    debug(f"{prefix}- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            debug(f"{prefix}  - Left side is smaller, so inputs are in the right order")
            return 1
        elif left == right:
            return 0
        else:
            debug(f"{prefix}  - Right side is smaller, so inputs are not in the right order")
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if len(right) <= i:
                debug(f"{prefix}  - Right side ran out of items, so inputs are not in the right order")
                return -1
            x = compare(left[i], right[i], depth+1)
            if not x == 0:
                return x
        if len(right) > len(left):
            debug(f"{prefix}  - Left side ran out of items, so inputs are in the right order")
            return 1
        return 0
    elif isinstance(left, int):
        debug(f"{prefix}  - Mixed types; convert left to [{left}] and retry comparison")
        return compare([left], right, depth+1)
    elif isinstance(right, int):
        debug(f"{prefix}  - Mixed types; convert right to [{right}] and retry comparison")
        return compare(left, [right], depth+1)
    else:
        raise Exception(f"uncomparable:\n\tleft: {left}\n\tright: {right}")

correct = []
for i in range(len(f)):
    debug(f"== Pair {i+1} ==")
    correct.append(compare(eval(f[i][0]), eval(f[i][1])))
    debug()

p1 = sum([i+1 for i in range(len(correct)) if correct[i] == 1])

print(f"part 1: {p1}")

dividers = [[[2]],[[6]]]
l = sorted(dividers + [eval(pair[i]) for i in range(2) for pair in f], key=cmp_to_key(compare), reverse=True)

divider_indexes = [i+1 for i in range(len(l)) if l[i] in dividers]

p2 = prod(divider_indexes)

print(f"part 2: {p2}")