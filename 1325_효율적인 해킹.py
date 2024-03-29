from collections import deque
def bfs(x, y):
    count = 0
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and board[x][y]==1:
                count += 1
                q.append([nx, ny])
    return count

n, m = list(map(int, input().split()))
board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1
    board[b-1][a-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            answer = max(answer, bfs(x, y))
print(answer)
