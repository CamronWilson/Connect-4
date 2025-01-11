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
def botmove(sym):
    while True:
        c=random.randint(0,6)
        if len(board[c])<6:
            place(c,sym)
            print("botplayed: "+ str(c+1))
            break

def place(col, sym):
    board[col].append(sym)

# print (board)
# board[0] = ['x']
# board[1] = ['o','o']
drawboard()

for i in range (21):
    botmove("x")
    drawboard()
    botmove("o")
    drawboard()
    # print()