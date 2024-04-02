def distance(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2

def interaction():
    return

def scollision(sdir):
    sn = board[rx][ry]
    board[rx][ry] = 0
    sx, sy, sc = santas[sn]

    sc += d
    sx -= drx[sdir]*d
    sy -= dry[sdir]*d

    if 1<=sx<=n and 1<=sy<=n:
        if board[sx][sy]!=0:
            interaction()
        else:
            santas[sn] = [sx, sy, sc]
    else:
        scores[sn] = sc
        santas[sn] = [sx, sy, -1]

    return

def rcollision(rdir):
    sn = board[rx][ry]
    board[rx][ry] = 0
    sx, sy, sc = santas[sn]

    sc += c
    sx += drx[rdir]*c
    sy += dry[rdir]*c

    if 1<=sx<=n and 1<=sy<=n:
        if board[sx][sy]!=0:
            interaction()
        else:
            santas[sn] = [sx, sy, sc]
    else:
        scores[sn] = sc
        santas[sn] = [sx, sy, -1]

def smove(sn):
    sdir = 0
    return sdir

def rmove():
    rdir = 0
    return rdir

def play():
    # 루돌프의 움직임, 루돌프 과실 충돌
    rdir = rmove()
    if board[rx][ry]!=0:
        rcollision(rdir)

    # 산타들의 움직임, 산타 과실 충돌
    for sn in range(1, p+1):
        sdir = smove(sn)
        if board[rx][ry]!=0:
            scollision(sdir)
    return

n, m, p, c, d = map(int, input().split())
rx, ry = map(int, input().split())

drx = [-1, 1, 0, 0, -1, -1, 1, 1]
dry = [0, 0, -1, 1, -1, 1, -1, 1]

santas = []
board = [[0 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(p):
    sn, sx, sy = map(int, input().split())
    santas[sn] = [sx, sy]
    board[sx][sy] = sn

# 산타별 점수
scores = [0]*(p+1)

# 게임판의 구성
for _ in range(m):
    play()