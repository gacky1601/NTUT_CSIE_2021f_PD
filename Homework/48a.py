def isWin(board):
    for i in range(1,9,3):
        if board[i]>0:
            if board[i]==board[i+1] and board[i]==board[i+2]:
                return board[i]
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6]:
            return board[i]
    if board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
            return board[5]
    for i in range(1,10):
        if board[i]==0:
            return 0 # Undecided
    return 3 # tie

def getBest(board,p):
    #print(board,p)
    
    for i in range(1,10):
        if board[i]==0:
            board[i] = p
            if isWin(board)==p: 
                return i
            board[i] = 0
    for i in range(1,10):
        if board[i]==0:
            board[i] = (p&1)+1
            if isWin(board)==(p&1)+1:
                return i
            board[i] = 0
    t = []
    if board[2]==1 and board[4]==1:
        t = [1,3,7]
    if board[2]==1 and board[6]==1:
        t = [1,3,9]
    if board[4]==1 and board[8]==1:
        t = [1,7,9]
    if board[6]==1 and board[8]==1:
        t = [3,7,9]
    for i in t:
        if board[i]==0:
            return i
    t = [5,1,3,7,9,2,4,6,8]
    for i in t:
        if board[i]==0:
            print(isWin(board))
            return i

def printBoard(board):
    for i in range(0,9,3):
        for j in range(1,4):
            print(board[i+j],end=' ')
        print()

def main():
    board = [0 for i in range(10)]
    m = int(input())
    move = [int(i) for i in input().split()]
    flag = True
    print(move)
    for i in range(len(move)):
        if board[move[i]]!=0:
            print("Error")
            flag = False
            continue
        board[move[i]] = m
        if isWin(board)!=0:
            break
        m = (m&1)+1
    if flag:
        print('OK')
    printBoard(board)
    d = {
        0 : "Undecided",
        1 : "Player win",
        2 : "Computer win",
        3 : "Tie"
    }
    t = isWin(board)
    print(d[t])
    if t==0:
        print(getBest(board,2))
main()