from statistics import median, mean

f = open('input/day07.txt', 'r').read().splitlines()[0]
# f = "16,1,2,0,4,2,7,1,2,14"
positions = [int(x) for x in f.split(",")]

min_pos = min(positions)
max_pos = max(positions)
med_pos = int(median(positions))
mean_pos = int(mean(positions))

med_diffs = [abs(x-med_pos) for x in positions]

print(sum(med_diffs))

diffs = [sum([sum(range(abs(x-target)+1)) for x in positions]) for target in range(mean_pos, mean_pos+2)]

print(min(diffs))