
def moveKnight(i, d):
    # 체력이 0 이하인 경우
    if k[i] <= 0:
        return

    #기사[i]가 움직일 수 있는 경우
    if canMoveKnight(i, d):

        for i in range(1, n+1):

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

l, n, q = map(int, input().split())

maxL = 41 #최대 보드 크기
maxN = 31 #최대 기사 수

board = []
for _ in range(l):
    board.append(list(map(int, input().split())))
board = [2 for _ in range(l+2)]+board+[2 for _ in range(l+2)]

initK = [0]*maxN #초기 체력
r = [0]*maxN
c = [0]*maxN
h = [0]*maxN
w = [0]*maxN
k = [0]*maxN
nr = [0]*maxN
nc = [0]*maxN
dmg = [0]*maxN
isMoved = [0]*maxN

# 기사 번호에 따른 각각의 정보
for i in range(1, n+1):
    r[i],c[i],h[i],w[i],k[i] = map(int, input().split())
    initK[i] = k[i]

# q개의 왕의 명령
for _ in range(q):
    i, d = map(int, input().split())
    moveKnight(i, d)
