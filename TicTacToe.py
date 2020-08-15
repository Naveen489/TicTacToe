board = {
    'A':' ', 'B':' ', 'C':' ',
    'D':' ', 'E':' ', 'F':' ',
    'G':' ', 'H':' ', 'I':' '
}
def print_xo(board):
    print(board['A'] + '|' + board['B'] + '|' + board['C'])
    print('-+-+-')
    print(board['D'] + '|' + board['E'] + '|' + board['F'])
    print('-+-+-')
    print(board['G'] + '|' + board['H'] + '|' + board['I'])

def check(board):
    if board['A'] == board['B'] == board['C'] == 'X' or board['A'] == board['B'] == board['C'] == 'O':
        return 1
    elif board['D'] == board['E'] == board['F'] == 'X' or board['D'] == board['E'] == board['F'] == 'O':
        return 1
    elif board['G'] == board['H'] == board['I'] == 'X' or board['G'] == board['H'] == board['I'] == 'O':
        return 1
    elif board['A'] == board['D'] == board['G'] == 'X' or board['A'] == board['D'] == board['G'] == 'O':
        return 1
    elif board['B'] == board['E'] == board['H'] == 'X' or board['B'] == board['E'] == board['H'] == 'O':
        return 1
    elif board['C'] == board['F'] == board['I'] == 'X' or board['C'] == board['F'] == board['I'] == 'O':
        return 1
    elif board['A'] == board['E'] == board['I'] == 'X' or board['A'] == board['E'] == board['I'] == 'O':
        return 1
    elif board['C'] == board['E'] == board['G'] == 'X' or board['C'] == board['E'] == board['G'] == 'O':
        return 1

print(" ")
print('A' + '|' + 'B' + '|' +'C')
print('-+-+-')
print('D' + '|' + 'E' + '|' +'F')
print('-+-+-')
print('G' + '|' + 'H' + '|' +'I')
print("These are the keys you have to enter to occupy the respestive spot")
print("Choose wisely and have fun!")
print("P.S. Turning on caps lock would be recommended")
print(" ")

total_moves = 0
player = 1

while True:
    print_xo(board)
    if total_moves == 9:
        print("It's a tie!")
        break
    elif check(board) == 1:
        print("You won!")
        break
    while True:
        if player == 1:
            p1_input = input("Player one: ")
            if p1_input in board and board[p1_input] == ' ':
                board[p1_input] = 'X'
                player = 2
                break
            else:
                print("Nope, try again")
                continue
        else:
            p2_input = input("Player two: ")
            if p2_input in board and board[p2_input] == ' ':
                board[p2_input] = 'O'
                player = 1
                break
            else:
                print("Nope, try again")
                continue
    total_moves += 1
    print(" ")