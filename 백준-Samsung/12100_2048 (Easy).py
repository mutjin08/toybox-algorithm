from copy import deepcopy

def boardPrint(board):
    print("-----")
    for b in board:
        print(*b)
    print("-----")

def right(before):
    board = deepcopy(before)
    for x, line in enumerate(board):
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
        newLine.reverse()
        newLine = [0]*(n-len(newLine))+newLine
        for y in range(n):
            board[x][y] = newLine[y]
    return board

def left(before):
    board = deepcopy(before)
    for x, line in enumerate(board):
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
        for y in range(n):
            board[x][y] = newLine[y]
    return board

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
        newLine.reverse()
        newLine = [0]*(n-len(newLine))+newLine
        for x in range(n):
            board[x][y] = newLine[x]
    return board

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
    return board

def iterate(stage, board):
    if stage>5:
        global answer
        answer = max(answer, max(map(max, board)))
        return

    iterate(stage+1,right(board))
    iterate(stage+1,left(board))
    iterate(stage+1,up(board))
    iterate(stage+1,down(board))


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = -1
iterate(1, board)
print(answer)