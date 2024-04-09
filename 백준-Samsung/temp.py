n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for idx, line in enumerate(board):
    print(idx)
    print(line)
    print("-----")

print(max(map(max, board)))