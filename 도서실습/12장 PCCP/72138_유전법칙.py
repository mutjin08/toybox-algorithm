def find(n, p):
    n -= 1
    p -= 1
    
    stack = []
    while n>0:
        stack.append(p%4)
        n-=1
        p//=4
    while stack:
        x = stack.pop()
        if x==0:
            return "RR"
        elif x==3:
            return "rr"
    return "Rr"

def solution(queries):
    answer = []
    for n, p in queries:
        answer.append(find(n, p))
    return answer