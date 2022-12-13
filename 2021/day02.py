f = open('input/day02.txt', 'r')
list = [x.split() for x in f]
horizontal = 0
depth = 0
for command in list:
    cmd = command[0]
    dist = int(command[1])
    if cmd == 'down':
        depth += dist
    elif cmd == 'up':
        depth -= dist
    else:
        horizontal += dist
print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0
for command in list:
    cmd = command[0]
    dist = int(command[1])
    if cmd == 'down':
        aim += dist
    elif cmd == 'up':
        aim -= dist
    else:
        horizontal += dist
        depth += (aim * dist)
print(horizontal * depth)
            