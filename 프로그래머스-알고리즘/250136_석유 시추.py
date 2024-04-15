from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isRange(x, y):
    global n, m
    if 0<=x<n and 0<=y<m:
        return True
    return False

def suck(x, y, land, visited):
    q = deque([[x, y]])
    visited[x][y] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isRange(nx, ny) and land[nx][ny]==1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny]=1
                count += 1
    return count
            
def solution(land):
    global n, m
    n, m = len(land), len(land[0])
    counts = []
    for y in range(m):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        count = 0
        for x in range(n):
            if land[x][y]==1 and not visited[x][y]:
                count += suck(x, y, land, visited)
        counts.append(count)
    return max(counts)