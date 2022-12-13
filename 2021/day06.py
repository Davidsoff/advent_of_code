from collections import Counter

f = open('input/day06.txt', 'r')
lines = [line for line in f]
fish = [int(x) for x in lines[0].split(',')]
normal = Counter(range(0,7))
normal.subtract(range(0,7))
normal.update(fish)
normal = dict(normal)
young = Counter([])
young = {7:0, 8:0}

for i in range(0,80):
    step = i % 7
    next = normal[step]
    normal[step] = normal[step] + young[7]
    young[7] = young[8]
    young[8] = next
print(sum(normal.values()) + sum(young.values()))

for i in range(80,256):
    step = i % 7
    next = normal[step]
    normal[step] = normal[step] + young[7]
    young[7] = young[8]
    young[8] = next
print(sum(normal.values()) + sum(young.values()))
