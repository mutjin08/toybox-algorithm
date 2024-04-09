def roll(dir, dice):
    #동쪽
    if dir==1:
        idx = [i-1 for i in [4, 2, 1, 6, 5, 3]]
        dice = [dice[i] for i in idx]
    #서쪽
    elif dir==2:
        idx = [i-1 for i in [3, 2, 6, 1, 5, 4]]
        dice = [dice[i] for i in idx]
    #북쪽
    if dir==3:
        idx = [i-1 for i in [5, 1, 3, 4, 6 ,2]]
        dice = [dice[i] for i in idx]
    #남쪽
    elif dir==4:
        idx = [i-1 for i in [2, 6, 3, 4, 1, 5]]
        dice = [dice[i] for i in idx]
    return dice


n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

for direction in commands:
    x += dx[direction-1]
    y += dy[direction-1]
    
    #만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
    if not (0<=x<n and 0<=y<m):
        x -= dx[direction-1]
        y -= dy[direction-1]
        continue
    
    dice = roll(direction, dice)
    #이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
    if board[x][y]==0:
        board[x][y]=dice[-1]
    #0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    else:
        dice[-1]=board[x][y]
        board[x][y]=0
    
    print(dice[0])