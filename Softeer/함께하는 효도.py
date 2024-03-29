import sys
input = sys.stdin.readline

from itertools import product

n, m = list(map(int, input().split()))

yields = []
for _ in range(n):
    yields.append(list(map(int, input().split())))


friends = []
for _ in range(m):
    friends.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtracking(depth, before, visited):
    if depth>3:
        print(visited)
        return
    
    after = []
    for x, y in before:
        person = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                person.append([nx, ny])
        after.append(person)
    
    for case in product(*after):
        case = list(case)
        backtracking(depth+1, case, friends+case)

backtracking(1, friends, friends)