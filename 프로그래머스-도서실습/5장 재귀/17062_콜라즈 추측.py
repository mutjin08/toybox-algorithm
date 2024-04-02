answer = 0
def solution(num):
    global answer
    if answer > 500:
        return -1
    if num==1:
        return answer
    
    answer += 1
    if num%2==0:
        num//=2
    else:
        num = num*3+1
    return solution(num)