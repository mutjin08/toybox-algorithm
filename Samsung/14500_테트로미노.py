def dfs(x, y, depth, score):
    global answer
    # 조기종료
    if answer >= score + maxValue*(4-depth):
        return

    if depth >= 4:
        answer = max(answer, score)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            # idx가 2일 때 (두 개의 블럭을 선택했을 때) 새로운 블럭에서 다음 블럭을 탐색하는 것이 아니라 다시 기존블럭에서 탐색하게 만들면 ㅗ 모양을 만들 수 있다
            if depth==2:
                visited[nx][ny] = 1
                dfs(x, y, depth+1, score+board[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, depth+1, score+board[nx][ny])
            visited[nx][ny] = 0

n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
maxValue = max(map(max, board))
answer = -1
visited = [[0 for _ in range(m)] for _ in range(n)]

for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(x, y, 1, board[x][y])
        visited[x][y] = 0

print(answer)