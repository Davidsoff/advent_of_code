f = open('input/day01.txt', 'r')
# f = open('input/test.txt', 'r')
list = [int(x) for x in f]
print(len([x for ind, x in enumerate(list) if ind > 0 and x > list[ind-1]]))

window_size = 3
sums = [sum(list[i: i + window_size]) for i in range(len(list) - window_size + 1)]
print(len([x for ind, x in enumerate(sums) if ind > 0 and x > sums[ind-1]])) 