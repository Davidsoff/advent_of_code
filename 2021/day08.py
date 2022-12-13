f = open('input/day08.txt', 'r').read().splitlines()
# f = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# """.splitlines()
input = [x.split(" | ") for x in f]
input = [(x[0].split(" "), x[1].split(" ")) for x in input]
count = 0
summed = 0
for line in input:
    key = [set(x) for x in line[0]]
    code = [set(x) for x in line[1]]

    one = [x for x in key if len(x) == 2][0]
    four = [x for x in key if len(x) == 4][0]
    seven = [x for x in key if len(x) == 3][0]
    eight = [x for x in key if len(x) == 7][0]

    
    three = [x for x in key if len(x) == 5 and x.intersection(seven) == seven][0]
    six = [x for x in key if len(x) == 6 and x.intersection(one) != one][0]
    
    inter = three.intersection(six)

    nine = [x for x in key if len(x) == 6 and x.intersection(inter) == inter and x.intersection(six) != six][0]
    zero = [x for x in key if len(x) == 6 and x.intersection(inter) != inter][0]

    two = [x for x in key if len(x) == 5 and x.intersection(inter) != inter][0]
    five = [x for x in key if len(x) == 5 and x.intersection(inter) == inter and x.intersection(three) != three][0]


    matches = [x for x in code if len(x) in [2,3,4,7]]
    count += len(matches)

    decoder = [zero, one, two, three, four, five, six, seven, eight, nine]
    res= "".join([str(decoder.index(x)) for x in code])
    summed += int(res)

print(count)
print(summed)