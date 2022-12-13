import itertools
f = [line[:-1] for line in open('input/day03.txt', 'r')]

def convert_to_prio(item):
    value = ord(item)
    if value > 95:
        return value - 96
    else:
        return 27+ (value - 65)

def grouped(iterable, n):
  return zip(*[iter([set(line) for line in iterable])]*n)


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def get_shared(rucksack):
    half = len(rucksack)//2
    c1 = [convert_to_prio(x) for x in set(rucksack[:half])]
    c2 = [convert_to_prio(x) for x in set(rucksack[half:])]
    return intersection(c1, c2)

shared_items = [ get_shared(line) for line in f]
flattened = list(itertools.chain(*shared_items))
print("part 1: ", sum(flattened))
print()

badges = [intersection(l1, intersection(l2, l3)) for l1, l2, l3 in grouped(f,3)]
flattened_badges = list(itertools.chain(*badges))
print("part 2: ", sum([convert_to_prio(x) for x in flattened_badges])) 



