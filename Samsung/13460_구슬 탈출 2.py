from collections import deque
def play(rx, ry, bx, by):
    q = deque([[rx, ry, bx, by]])
    visited = {}
    visited[" ".join(map(str, [rx, ry, bx, by]))] = 1
    
    for cnt in range(1, 11):
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            for i in range(4):
                #blue
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby]=="O":
                        break
                    if board[nbx][nby]=="#":
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                #blue succeed
                if board[nbx][nby]=="O":
                    continue

                #red
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry]=="O":
                        break
                    if board[nrx][nry]=="#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                #red succeed
                if board[nrx][nry]=="O":
                    return cnt
                
                #overlapped
                if nrx==nbx and nry==nby:
                    if abs(rx-nrx)+abs(ry-nry) > abs(bx-nbx)+abs(by-nby):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                log = " ".join(map(str, [nrx, nry, nbx, nby]))
                if log in visited:
                    continue
                q.append([nrx, nry, nbx, nby])
                visited[log] = 1
    return -1
            

n, m = list(map(int, input().split()))
board = []
for x in range(n):
    board.append(input())
    for y in range(m):
        if board[x][y]=="B":
            bx, by = x, y
        elif board[x][y]=="R":
            rx, ry = x, y

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(play(rx, ry, bx, by))