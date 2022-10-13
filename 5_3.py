# Создайте программу для игры в 'Крестики-нолики'.

board = list(range(1, 10))

win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
            (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def print_board():
    print("-------------")
    for i in range(3):
        print(f"|", board[0 + i*3], "|",
              board[1 + i*3], "|", board[2 + i*3], "|")
    print("-------------")


def symbol_input(symbol):
    while True:
        value = input(f'где будет стоять {symbol} => ')
        if not(value in '123456789'):
            print("Ошибка ввода, повторите попытку!")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка занята')
            continue
        board[value - 1] = symbol
        break


def winner():
    for i in win_comb:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1] - 1]
    else:
        return False


def result():
    counter = 0
    while True:
        print_board()
        if counter % 2 == 0:
            symbol_input('X')
        else:
            symbol_input("O")
        if counter > 3:
            win = winner()
            if win:
                print_board()
                print(win, 'выиграл!!!')
                break
        counter += 1
        if counter > 8:
            print_board()
            print("Победила дружба!")
            break


result()
