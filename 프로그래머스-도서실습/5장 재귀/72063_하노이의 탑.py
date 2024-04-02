def hanoi(n, left, mid, right):
    if n==1:
        return [[left, right]]
    answer = hanoi(n-1, left, right, mid)
    answer += hanoi(1, left, mid, right)
    answer += hanoi(n-1, mid, left, right)
    return answer

def solution(n):
    return hanoi(n, 1, 2, 3)