import itertools
raw = open('input/day05.txt', 'r')
# raw = open('input/test.txt', 'r')
f = raw.read()

class State(object):
    stacks = []

    def __init__(self, input_str):
        layers = [[s[i+1:i+2] for i in range(0, len(s), 4)] for s in input_str.splitlines()[:-1]]
        self.stacks = [[] for _ in range(len(layers[0]))]
        for layer in layers[::-1]:
            for i in range(len(layer)):
                if(layer[i] != " "):
                    self.stacks[i].append(layer[i])

    def make_move_p1(self, move):
        for _ in range(move.amount):
            self.stacks[move.target].append(self.stacks[move.source].pop())

    def make_move_p2(self, move):
        tmp = []
        for _ in range(move.amount):
            tmp.append(self.stacks[move.source].pop())
        for i in tmp[::-1]:
            self.stacks[move.target].append(i)
    
    def get_message(self):
        return ''.join([ stack[-1] for stack in self.stacks ])
    
    def __str__(self):
        return str(self.stacks)

class Move(object):
    amount = 0
    source = 0
    target = 0

    def __init__(self, input_str):
        l = input_str.split(" ")
        self.amount = int(l[1])
        self.source = int(l[3])-1
        self.target = int(l[5])-1
    
    def __str__(self):
        return f"move {self.amount} from {self.source + 1} to {self.target + 1}"
    
    def __repr__(self):
        return str(self)

parts = f.split("\n\n")

state = State(parts[0])
procedure = [ Move(line) for line in parts[1].splitlines() ]

print("starting state:")
print(state)
print("\nprocedure:")
for move in procedure:
    print(move)
    state.make_move_p1(move)
print("final state:")
print(state)
print()

p1 = state.get_message()

print("part 1: ", p1)

state = State(parts[0])

print("starting state:")
print(state)
print("\nprocedure:")
for move in procedure:
    state.make_move_p2(move)
print("final state:")
print(state)
print()

p2 = state.get_message()

print("part 2: ", p2)