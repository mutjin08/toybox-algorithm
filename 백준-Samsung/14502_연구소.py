from collections import deque
from copy import deepcopy

def countSafe():
    spread = deepcopy(board)
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and spread[nx][ny]==0:
                spread[nx][ny]=2
                q.append([nx, ny])

    answer = 0
    for x in range(n):
        for y in range(m):
            if spread[x][y]==0:
                answer += 1
    return answer

def buildWall(depth):
    if depth==3:
        global answer
        answer = max(answer, countSafe())
        return

    for x in range(n):
        for y in range(m):
            if board[x][y]==0:
                board[x][y]=1
                buildWall(depth+1)
                board[x][y]=0

n, m = list(map(int, input().split()))
board = []
virus = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y]==2:
            virus.append([x, y])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
buildWall(0)
print(answer)