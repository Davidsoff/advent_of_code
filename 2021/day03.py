f = open('input/day03.txt', 'r')
list = [x for x in f]
epsilon = 0
gamma = 0
chars = [0] * (len(list[0])-1)
mask = int(''.join(['1'] * (-1+len(list[0]))), 2)
half = 500
for line in list:
    for index, char in enumerate(line):
        if char == "1":
            chars[index] += 1
res = ''.join(['1' if x>half else '0' for x in chars])
epsilon = int(res,2)
gamma = epsilon ^ mask

print(gamma*epsilon)

oxygen = list
i = 0
size = len(oxygen)
length = len(oxygen[0])
while size > 1 and i < length:
    half = size/2
    ones = 0
    for line in oxygen:
        if line[i] == '1':
            ones = ones + 1
    most_common = '1' if ones >= half else '0'
    oxygen = [ x for x in oxygen if x[i]==most_common]
    size = len(oxygen)
    i = i+1
print(oxygen[0])

co2 = list
i = 0
size = len(co2)
length = len(co2[0])
while size > 1 and i < length:
    half = size/2
    ones = 0
    for line in co2:
        if line[i] == '1':
            ones = ones + 1
    least_common = '0' if ones >= half else '1'
    co2 = [ x for x in co2 if x[i]==least_common]
    size = len(co2)
    i = i+1

print(co2[0])

ans = int(oxygen[0],2) * int(co2[0],2)
print(ans)