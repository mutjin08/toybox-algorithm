def distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def play():
    peopleBoard = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for x, y in people:
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #보드 벗어난 경우
            if not (1<=nx<=n and 1<=ny<=n):
                continue
            #벽인 경우
            if board[nx][ny]>0:
                continue
            #이동 후 최단거리가 멀어지거나 같은 경우
            if distance(ex, ey, x, y) <= distance(ex, ey, nx, ny):
                continue

            if peopleBoard[nx][ny]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = [[0 for _ in range(n+1)]]
for _ in range(n):
    board.append([0]+list(map(int, input().split())))
people = []
for _ in range(m):
    people.append(list(map(int, input().split())))
ex, ey = map(int, input().split())

for _ in range(n):
    play()

    # all escaped
    if not len(people):
        break