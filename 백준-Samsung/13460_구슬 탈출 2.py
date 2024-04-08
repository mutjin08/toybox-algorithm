from collections import deque
def distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def play(rx, ry, bx, by):
    q = deque([[rx, ry, bx, by]])
    visited = {}
    visited[" ".join(map(str, [rx, ry, bx, by]))]=1
    for stage in range(1, 11):
        for _ in range(len(q)):
            
            rx, ry, bx, by = q.popleft()

            for i in range(4):
                # red move
                nrx, nry = rx, ry
                while True:
                    if board[nrx][nry]=="#" or board[nrx][nry]=="O":
                        break
                    nrx+=dx[i]
                    nry+=dy[i]
                if board[nrx][nry]=="#":
                    nrx-=dx[i]
                    nry-=dy[i]

                #blue move
                nbx, nby = bx, by
                while True:
                    if board[nbx][nby]=="#" or board[nbx][nby]=="O":
                        break
                    nbx+=dx[i]
                    nby+=dy[i]
                if board[nbx][nby]=="O":
                    continue
                if board[nbx][nby]=="#":
                    nbx-=dx[i]
                    nby-=dy[i]

                #overlapped
                if nrx==nbx and nry==nby:
                    if distance(nrx, nry, rx, ry) < distance(nbx, nby, bx, by):
                        nbx-=dx[i]
                        nby-=dy[i]
                
                # red succeed
                if board[nrx][nry]=="O":
                    return stage

                # blue succeed
                if board[nbx][nby]=="O":
                    continue

                if " ".join(map(str, [nrx, nry, nbx, nby])) not in visited:
                    q.append([nrx, nry, nbx, nby])           
    return -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
for x in range(n):
    board.append(input())
    for y in range(m):
        if board[x][y]=="B":
            bx, by = x, y
        elif board[x][y]=="R":
            rx, ry = x, y

print(play(rx, ry, bx, by))