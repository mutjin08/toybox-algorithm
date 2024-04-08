from copy import deepcopy

def down(before):
    board = deepcopy(before)
    for y, line in enumerate(zip(*board)):
        line = [i for i in line if i!=0]
        newLine = []
        while len(line)>=2:
            if line[-1]==line[-2]:
                newLine.append(line[-1]*2)
                line.pop()
                line.pop()
            else:
                newLine.append(line[-1])
                line.pop()
        newLine += line
        newLine = [0]*(n-len(newLine))+newLine
        for x in range(n-1, -1, -1):
            board[x][y] = newLine[x]
    for b in board:
        print(*b)

def up(before):
    board = deepcopy(before)
    for y, line in enumerate(zip(*board)):
        line = [i for i in line if i!=0]
        newLine = []
        while len(line)>=2:
            if line[0]==line[1]:
                newLine.append(line[0]*2)
                line.pop(0)
                line.pop(0)
            else:
                newLine.append(line[0])
                line.pop(0)
        newLine += line
        newLine = newLine + [0]*(n-len(newLine))
        for x in range(n):
            board[x][y] = newLine[x]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

down(board)