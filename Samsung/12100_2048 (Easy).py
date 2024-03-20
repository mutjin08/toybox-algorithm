from copy import deepcopy

def down(before):
    board = deepcopy(before)
    for y in range(n):
        for x in range(n-1, -1, -1):
            if board[x][y]==0:
                for nx in range(x-1, -1, -1):
                    board[nx+1][y] = board[nx][y]
                board[0][y] = 0

            for nx in range(x-1, -1, -1):
                if board[nx][y]!=0:
                    if board[x][y]==board[nx][y]:
                        board[x][y]*=2
                        board[nx][y]=0
                    break
            if y==3:
                print(board)
    return board

def up(before):
    board = deepcopy(before)
    for y in range(n):
        for x in range(n):
            if board[x][y]==0:
                for nx in range(x+1, n):
                    board[nx-1][y] = board[nx][y]
                board[n-1][y] = 0

            for nx in range(x+1, n):
                if board[nx][y]!=0:
                    if board[x][y]==board[nx][y]:
                        board[x][y]*=2
                        board[nx][y]=0
                    break
    return board

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

print(down(board))