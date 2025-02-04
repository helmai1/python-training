board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    # mengisi array board atau mengisi huruf
    board[pos] = letter

# kondisi tempat jika masih kosong
def spaceIsFree(pos):
    return board[pos] == ' '

# Template papan
def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    # Untuk mengecek apakah board tersebut sudah terisi atau full
    if board.count(' ')>1:
        return False
    else:
        return True

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] and b[9] == l)or
    #kebawah
    (b[1] == l and b[4] == l and b[7] == l)or
    (b[2] == l and b[5] == l and b[8] == l)or
    (b[3] == l and b[6] == l and b[9] == l)or
    #miring
    (b[1] == l and b[5] == l and b[9] == l)or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run  = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry this space is occupied')
            else:
                ('please type a number between 1 and 9')
        except Exception as e:
            print('Please type a number')

#pergerakan bot atau AI
def computerMove():
    possibleMove = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMove:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMove:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMove:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMove:
        if i in (2, 4, 6, 8):
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you loose!")
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O', move)
                print('computer placed an o on position', move, ":")
                printBoard(board)
        else:
            print("You win!")
            break


    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() ==  'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
