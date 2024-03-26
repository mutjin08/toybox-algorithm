def to1dim(board, x1, y1, x2, y2):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 1]
    temp = []
    
    nx, ny = x1, y1-1
    for i in range(4):
        if i%2==0:
            for _ in range(y2-y1+1):
                nx += dx[i]
                ny += dy[i]
                temp.append(board[nx][ny])
        else:
            for _ in range(x2-x1+1):
                nx += dx[i]
                ny += dy[i]
                temp.append(board[nx][ny])
    return temp
                

def spin(board, x1, y1, x2, y2):
    
    return to1dim(board, x1, y1, x2, y2)

def solution(rows, columns, queries):
    board = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    print(board)
    for q in queries:
        x1, y1, x2, y2 = q
        board = spin(board, x1-1, y1-1, x2-1, y2-1)
        break
    return boards