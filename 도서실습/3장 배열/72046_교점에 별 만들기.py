from itertools import combinations

def draw(spots):
    valX, valY = zip(*spots)
    minX, minY = min(valX), min(valY)
    maxX, maxY = max(valX), max(valY)
    sizeX, sizeY = maxX-minX+1, maxY-minY+1
    
    board = [["." for _ in range(sizeX)] for _ in range(sizeY)]
    for x, y in spots:
        y -= minY
        x -= minX
        board[y][x]="*"
    
    return ["".join(b) for b in board[::-1]]

def solution(line):
    commonSpots = []
    for line1, line2 in combinations(line, 2):
        a, b, e = line1
        c, d, f = line2
        if (a*d-b*c)==0:
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if x%1==0 and y%1==0:
            commonSpots.append((int(x), int(y)))
    commonSpots = list(set(commonSpots))
    return draw(commonSpots)
    
    