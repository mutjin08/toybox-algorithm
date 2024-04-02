def interaction():
    print("interaction!!!")
    return

def scrash(sdir):
    return

def smove(sn):
    sdir = 1
    return sdir

def rcrash(rdir):
    sn = board[rx][ry]
    sx, sy, sc = santas[sn]
    
    #산타는 c만큼의 점수 획득
    sc += c

    #산타는 루돌프 이동방향으로 c만큼 밀려남
    board[sx][sy]=0
    sx += drx[rdir]*c
    sy += drx[rdir]*c

    #밀려난 위치가 게임판 밖이면 게임에서 탈락함
    if not (1<=sx<=n and 1<=sy<=n):
        print("overlapped!!!")
        scores[sn] = sc
        sc = -1
        santas[sn] = [sx, sy, sc]
        return
    
    #밀려난 위치에 다른 산타가 있으면 상호작용이 발생함
    if board[sx][sy]!=0:
        interaction()
    
    print("moved!!!")

def rmove():
    global rx, ry

    #가장 가까운 산타 찾기
    sdistances = []
    for sn in range(1, p+1):
        sx, sy, sc = santas[sn]
        sdistances.append([distance(sx, sy, rx, ry), sx, sy])
    sdistances.sort(key = lambda x : (x[0], -x[1], -x[2]))
    sdist, sx, sy = sdistances[0]
    
    #루돌프 돌진 방향 찾기
    rdirs = []
    for rdir in range(8):
        nrx = rx + drx[rdir]
        nry = ry + dry[rdir]
        if 1<=nrx<=n and 1<=nry<=n:
            rdirs.append([distance(sx, sy, nrx, nry), nrx, nry, rdir])
    rdirs.sort(key = lambda x : x[0])
    rdist, rx, ry, rdir = rdirs[0]

    return rdir

def distance(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2

def play():
    #루돌프의 움직임
    rdir = rmove()

    #루돌프 과실 충돌
    if board[rx][ry]!=0:
        rcrash(rdir)

    #산타의 움직임
    for sn in range(1, p+1):
        if santas[sn][2] < 0:
            continue
        sdir = smove(sn)
        #산타 과실 충돌
        if board[rx][ry]!=0:
            scrash(sdir)

#input
n, m, p, c, d = map(int, input().split())
rx, ry = map(int, input().split())

# 게임판의 구성
santas = {}
scores = [0 for _ in range(n+1)]
board = [[0 for _ in range(n+1)]for _ in range(n+1)]

for _ in range(p):
    sn, sx, sy = map(int, input().split())
    santas[sn] = [sx, sy, 0] #x, y, score
    board[sx][sy] = sn

# 루돌프의 이동 방향
drx = [-1, 1, 0, 0, -1, -1, 1, 1]
dry = [0, 0, -1, 1, -1, 1, -1, 1]

# 산타의 이동 방향
dsx = []
dsy = []

for _ in range(m):
    play()

