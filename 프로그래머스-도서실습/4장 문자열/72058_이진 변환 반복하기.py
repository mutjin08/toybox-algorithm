def toBin(n):
    answer = ""
    while n > 0:
        answer = str(n%2) + answer
        n //= 2
    return answer

def solution(x):
    answer = [0, 0]
    while x != "1":
        answer[0] += 1
        answer[1] += len(x)
        x = x.replace("0","")
        answer[1] -= len(x)
        c = len(x)
        x = toBin(c)
    return answer