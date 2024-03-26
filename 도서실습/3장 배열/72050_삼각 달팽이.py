def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    idx = 1
    for i in range(n):
        for _ in range(n-i):
            x += dx[i%3]
            y += dy[i%3]
            board[x][y] = idx
            idx += 1
        
    board = sum([board[i][:i+1] for i in range(n)], []) #flatten
    return board