board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def printboard():
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board)
