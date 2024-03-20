from collections import deque
def clean(x, y, d):
    answer = 0
    while 1:
        if board[x][y]==0:
            answer += 1
            board[x][y]=2
        
        needClean = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny]==0:
                needClean = 1
                break
        
        if not needClean:
            nx = x - dx[d]
            ny = y - dy[d]

            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]==1:
                    return answer
                x, y = nx, ny
                continue
        else:
            d = (d-1)%4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                x, y = nx, ny
                continue
    return answer


n, m = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
finish = 0
dx = [-1, 0, 1, 0]
dy = [0, 1 ,0, -1]

print(clean(r, c, d))