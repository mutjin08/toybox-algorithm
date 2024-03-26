def spin(board, x1, y1, x2, y2):
    numbers = []
    
    for y in range(y1, y2):
        numbers.append(board[x1][y])
    
    for x in range(x1, x2):
        numbers.append(board[x][y2])
        
    for y in range(y2, y1, -1):
        numbers.append(board[x2][y])
        
    for x in range(x2, x1, -1):
        numbers.append(board[x][y1])
    
    numbers = [numbers.pop()]+numbers
    idx = 0
    
    for y in range(y1, y2):
        board[x1][y] = numbers[idx]
        idx += 1
    
    for x in range(x1, x2):
        board[x][y2] = numbers[idx]
        idx += 1
        
    for y in range(y2, y1, -1):
        board[x2][y] = numbers[idx]
        idx += 1
        
    for x in range(x2, x1, -1):
        board[x][y1] = numbers[idx]
        idx += 1
    
    return board, min(numbers)
            
def solution(rows, columns, queries):
    board = [[y+x*columns+1 for y in range(columns)] for x in range(rows)]
    
    answer = []
    for x1, y1, x2, y2 in queries:
        board, minVal = spin(board, x1-1, y1-1, x2-1, y2-1)
        answer.append(minVal)
    return answer
        