import random

def check_pattern(start: int, end: int, count: int) -> int:
    player_scores: int = 0
    bot_scores: int = 0
    for i in range(start-1, end, count):
        if board[i] == 'X': player_scores += 1
        elif board[i] == 'O': bot_scores += 1
        else: 
            player_scores = 0
            bot_scores = 0
    # print(scores)
    if player_scores == 3:
        print('\nPlayer won!')
        return player_scores
    elif bot_scores == 3:
        print('\nBot won!')
        return bot_scores
    else:
        return 0

def bot_input() -> None:
    bot_coords: int = random.randint(0, 8)
    if board[bot_coords] == ' ':
        board[bot_coords] = 'O'
    else:
        bot_input()

def print_board() -> None:
    for i in range(len(board)):
        print(f'[{board[i]}]', end='')
        if i == 2: print()
        elif i == 5: print()

print('! TIC-TAC-TOE !')
print('[1][2][3]')
print('[4][5][6]')
print('[7][8][9]\n')

board: list[str] = []
for _ in range(9):
    board.append(' ')
print_board()

is_running: bool = True

while is_running:
    try:
        coordinate = input('\nEnter a number from 1 to 9 (q to quit): ')
        if coordinate == 'q': break

        coordinate = int(coordinate)
        if coordinate < 1 or coordinate > 9:
            print('Out of bounds')
        else:
            board[coordinate-1] = 'X'
            bot_input()
            print_board()
            if check_pattern(1, 3, 1) == 3: break   # horizontal
            elif check_pattern(4, 6, 1) == 3: break
            elif check_pattern(7, 9, 1) == 3: break
            elif check_pattern(1, 7, 3) == 3: break # vertical
            elif check_pattern(2, 8, 3) == 3: break
            elif check_pattern(3, 9, 3) == 3: break
            elif check_pattern(1, 9, 4) == 3: break # diagonal
            elif check_pattern(3, 8, 2) == 3: break
    except ValueError:
        print('Please enter a number only.')

input('Enter to quit')