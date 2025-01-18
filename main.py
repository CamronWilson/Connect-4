import random
board=[]
for i in range (7):
    board.append([])
def drawboard():
    for i in range(6):
        for collum in board:
            if len(collum)>5-i:
                print("["+collum[5-i]+"]", end='')
            else:
                print("[ ]",end='')
        print()
    print(" 1  2  3  4  5  6  7")

def botmove(sym):
    while True:
        c=random.randint(0,6)
        if len(board[c])<6:
            place(c,sym)
            print("botplayed: "+ str(c+1))
            break

def playermove(sym):
    while True:
        choice=input("Select a collum.")
        if choice in ["1","2","3","4","5","6","7"]:
            c=int(choice)-1
            if len(board[c])<6:
                place(c,sym)
                break

def place(col, sym):
    board[col].append(sym)
    print(checkwin(col, len(board[col])-1, sym))

def checkwin(col, row, sym):
    count=1
    if row>=3:#check down
        for i in range(3):
            if board[col][row-1-i]==sym:
                count=count+1
            else:
                break
        if count>=4:
            return True
    count=1
    for i in range (col-1,-1,-1):#check left
        if len(board[i])>row and board[i][row]==sym:
            count=count+1
        else:
            break
    if count>=4:
        return True
    
    for i in range (col+1,7,1):#check right
        if len(board[i])>row and board[i][row]==sym:
            count=count+1
        else:
            break
    if count>=4:
        return True
    
    count=1
    for i in range(1,4):#check diagonal up right
        if len(board[col+i])>row+i and board[col+i][row+i]==sym:
            count=count+1
        else:
            break
    if count>=4:
        return True
        
    return False
        

# print (board)
# board[0] = ['x']
# board[1] = ['o','o']
drawboard()

for i in range (21):
    playermove("x")
    drawboard()
    playermove("o")
    drawboard()

    # print()

