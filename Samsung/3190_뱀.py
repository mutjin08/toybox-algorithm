from collections import deque
n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x, y = list(map(int, input().split()))
    board[x-1][y-1] = 1 #apple

l = int(input())
changeDir = {}
for _ in range(l):
    x, c = input().split()
    if c=="D":
        changeDir[int(x)] = 1
    elif c=="L":
        changeDir[int(x)] = -1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move():
    snake = deque([[0, 0]])
    dir = 0
    currentTime = 0

    while snake:
        hx, hy = snake[-1]
        if currentTime in changeDir:
            dir = (dir+changeDir[currentTime])%4
        nx, ny = hx + dx[dir], hy + dy[dir]

        if not (0<=nx<n and 0<=ny<n):
            return currentTime + 1
        if board[nx][ny]==2:
            return currentTime + 1
        
        snake.append([nx, ny])
        if board[nx][ny]==1:
            board[nx][ny]=2
        elif board[nx][ny]==0:
            board[nx][ny]=2
            tx, ty = snake.popleft()
            board[tx][ty]=0
        currentTime += 1
    return currentTime + 1

print(move())