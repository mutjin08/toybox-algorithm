from copy import deepcopy
from collections import deque

def spreadVirus(before):
    board = deepcopy(before)
    q = deque(originalVirusPosition)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and and not visite board[nx][ny]==0:
                board[nx][ny] = 2
                q.append([nx, ny])
    return board

def countEmpty(board):
    empty = 0
    for b in board:
        empty+=b.count(0)
    return empty

def buildWall(wallCnt):
    if wallCnt >= 3:
        global answer
        answer = max(answer, countEmpty(spreadVirus(board)))
        return 
    
    for x in range(n):
        for y in range(m):
            if board[x][y]==0:
                board[x][y]=1
                buildWall(wallCnt+1)
                board[x][y]=0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

originalVirusPosition = []
for x in range(n):
    for y in range(m):
        if board[x][y]==2:
            originalVirusPosition.append([x, y])

answer = -1
buildWall(0)
print(answer)