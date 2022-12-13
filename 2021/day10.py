input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

input = open('input/day10.txt', 'r').read()
illegals = []
incomplete = []

for line in input.splitlines():
    reversed = list(line)[::-1]
    checked = []
    while len(reversed) > 0:
        char = reversed.pop()
        if char in ['(','[','{','<']:
            checked.append(char)
        else:
            last = checked.pop()
            if ((last != '(' and char == ')') or
                (last != '[' and char == ']') or
                (last != '{' and char == '}') or
                (last != '<' and char == '>')
            ):
                illegals.append(char)
                break
    if len(reversed) == 0:
        incomplete.append(line)

syntaxpoints = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

print(sum([syntaxpoints[c] for c in illegals]))

correctionpoints = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

def is_matching_pair(open, close):
    return ((open == '(' and close == ')') or
            (open == '[' and close == ']') or
            (open == '{' and close == '}') or
            (open == '<' and close == '>')
            )

final_score = []
for line in incomplete:
    checked = []
    score = 0
    for char in line[::-1]:
        if char in (')]}>'):
            checked.append(char)
        else:
            if len(checked) == 0:
                score = score * 5
                score = score + correctionpoints[char]
            else:
                checked.pop()
    final_score.append(score)

print(sorted(final_score)[len(final_score)//2])
