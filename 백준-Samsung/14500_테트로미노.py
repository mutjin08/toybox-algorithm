def place(blockCnt, blockSum, x, y):
    global answer
    #조기종료
    if answer >= blockSum+maxBlock*(4-blockCnt):
        return

    if blockCnt >= 4:
        answer = max(answer, blockSum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            #주의
            if blockCnt==2:
                visited[nx][ny]=1
                place(blockCnt+1, blockSum+board[nx][ny], x, y)
                visited[nx][ny]=0
            visited[nx][ny]=1
            place(blockCnt+1, blockSum+board[nx][ny], nx, ny)
            visited[nx][ny]=0


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]
maxBlock = max(map(max, board))
answer = -1
for x in range(n):
    for y in range(m):
        visited[x][y]=1
        place(1, board[x][y], x, y)
        visited[x][y]=0
print(answer)