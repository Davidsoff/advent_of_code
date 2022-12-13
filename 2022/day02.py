import itertools
f = open('input/day02.txt', 'r')

loss = 0
draw = 3
win = 6

move_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

opponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

player_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

def calculate_move(opponent, target):
    if target == "Y":
        return opponent
    elif opponent == "rock":
        return "paper" if target == "Z" else "scissors"
    elif opponent == "paper":
        return "scissors" if target == "Z" else "rock"
    elif opponent == "scissors":
        return "rock" if target == "Z" else "paper"
    

def get_score(opponent, player):   
    if opponent == player:
        result = draw
    elif player == "rock":
        if opponent == "paper":
            result = loss
        else:
            result = win
    elif player == "paper":
        if opponent == "scissors":
            result = loss
        else:
            result = win
    elif player == "scissors":
        if opponent == "rock":
            result = loss
        else:
            result = win

    return result + move_points[player]

splitted = [line.strip().split(" ") for line in f]
moves = [ [opponent_moves[game[0]], player_moves[game[1]]] for game in splitted ]
scores = [get_score(game[0], game[1]) for game in moves ]
print(sum(scores))

p2_moves = [ [opponent_moves[game[0]], calculate_move(opponent_moves[game[0]], game[1]) ] for game in splitted ]
p2_scores = [get_score(game[0], game[1]) for game in p2_moves ]
print(sum(p2_scores))