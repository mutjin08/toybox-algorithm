from collections import deque
def printBoard(board):
    print("-----")
    for b in board:
        print(*b)
    print("-----")

# 보드
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

# 사과의 위치
k = int(input())
apples = []
for _ in range(k):
    ax, ay = map(int, input().split())
    ax, ay = ax-1, ay-1
    board[ax][ay] = 2 #사과는 2
    apples.append([ax, ay])

# 뱀의 방향 전환
l = int(input())
changes = {}
for _ in range(l):
    x, c = input().split() #x초 후 c방향으로 전환
    changes[int(x)] = c

#뱀
snake = deque([[0, 0]])
sx, sy = 0, 0
sdir = 0
board[sx][sy] = 1 #뱀은 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#0초~time초 이동
time = 1
while True:
    #먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    sx += dx[sdir]
    sy += dy[sdir]

    #만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0<=sx<n and 0<=sy<n) or board[sx][sy]==1:
        break
    
    #만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[sx][sy]==2:
        snake.append([sx, sy])
        board[sx][sy]=1
    #만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        snake.append([sx, sy])
        tx, ty = snake.popleft()
        board[sx][sy]=1
        board[tx][ty]=0

    #게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
    if time in changes:
        turn = changes[time]
        if turn=="L":
            sdir = (sdir-1)%4
        elif turn=="D":
            sdir = (sdir+1)%4
    # 시간 증가
    time += 1
print(time)


    




