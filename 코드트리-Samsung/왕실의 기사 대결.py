def placeKnights():
    kboard = [[0 for _ in range(l+1)] for _ in range(l+1)]
    for i in range(1, n+1):
        r, c, h, w, k = knights[i]
        for x in range(r, r+h):
            for y in range(c, c+w):
                kboard[x][y] = i
    return kboard

def left(i):
    return

def right(i):
    return

def up(i):
    return

def down(i):
    return

l, n, q = map(int, input().split())
board = [[0 for _ in range(l+1)]]
for _ in range(l):
    board.append([0]+list(map(int, input().split())))

knights = {}
for i in range(1,n+1):
    knights[i] = list(map(int, input().split())) #r, c, h, w, k

for _ in range(q):
    i, d = map(int, input().split())
    
    if d==0:
        up(i)
    elif d==1:
        right(i)
    elif d==2:
        down(i)
    elif d==3:
        left(i)