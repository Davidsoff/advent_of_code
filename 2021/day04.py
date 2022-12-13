WIDTH = 5

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def print_board(board):
    print('\n'.join(' '.join(f"{x: >3}" for x in row) for row in chunks(board, WIDTH)))
    print()

def row(board, idx):
    row = idx//5
    offset = 5*row
    r = board[offset:offset+5]
    return r

def col(board, idx):
    col = idx % 5
    c = board[col::5]
    return c

def winner_row(board, idx):
    return  all(x>=100 for x in row(board, idx))

def winner_col(board, idx):
    return  all(x>=100 for x in col(board, idx))

def check_board(board, numbers):
    for number in numbers:
        try:
            idx = board.index(number)
            board[idx] += 100
            if winner_row(board, idx) or winner_col(board, idx):
                return numbers.index(number)
        except:
            continue

def get_unmarked_sum(board, numbers):
    unmarked = set(board)-set(numbers)
    return sum(unmarked)

f = open('input/day04.txt', 'r').read()
input = f.split("\n\n")

numbers, *boards = input
boards = [[int(x) for x in board.replace('\n', ' ').split(' ') if x !=''] for board in boards]
numbers = [int(x) for x in numbers.split(',')]

bingo_times = [check_board(board, numbers) for board in boards]
fastest_bingo_index = min(bingo_times)
fastest_bingo_value = numbers[fastest_bingo_index]

winner_idx = bingo_times.index(fastest_bingo_index)
winning_board = [x-100 if x>=100 else x for x in boards[winner_idx]]

winning_sum = get_unmarked_sum(winning_board, numbers[:fastest_bingo_index+1])
print(f"{winning_sum}*{fastest_bingo_value} = {winning_sum*fastest_bingo_value}")


slowest_bingo_index = max(bingo_times)
slowest_bingo_value = numbers[slowest_bingo_index]
loser_idx = bingo_times.index(slowest_bingo_index)
losing_board = [x-100 if x>=100 else x for x in boards[loser_idx]]

losing_sum = get_unmarked_sum(losing_board, numbers[:slowest_bingo_index+1])
print(f"{losing_sum}*{slowest_bingo_value} = {losing_sum*slowest_bingo_value}")