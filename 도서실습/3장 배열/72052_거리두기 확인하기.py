def isSafe(x, y, board):
    n = 5
    dx = [-1, 0, 1, 1, 1, 0, -1, -1, 2, -2, 0, 0]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0, 0, -2, 2]
    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny]=="P":
            
            isPartition = 0
            for mx in range(min(x, nx), max(x, nx)+1):
                for my in range(min(y, ny), max(y, ny)+1):
                    if board[mx][my]=="X":
                        isPartition = 1
            if not isPartition:
                return 0
    return 1

def check(board):
    n = 5
    for x in range(n):
        for y in range(n):
            if board[x][y]=="P" and not isSafe(x, y, board):
                return 0   
    return 1
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer