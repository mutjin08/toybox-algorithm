from itertools import combinations
def check(board):
    n = 5
    people = []
    for x in range(n):
        for y in range(n):
            if board[x][y]=="P":
                people.append([x, y])
                
    for a, b in combinations(people, 2):
        distance = abs(a[0]-b[0])+abs(a[1]-b[1])
        if distance == 1:
            return 0
        elif distance == 2:
            for x in range(min(a[0], b[0]), max(a[0], b[0])+1):
                for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
                    if board[x][y]=="O":
                        return 0
    return 1

def solution(places):
    answer = []
    for p in places:
        answer.append(check(p))
    return answer