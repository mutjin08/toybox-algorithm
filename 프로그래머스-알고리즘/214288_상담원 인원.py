from itertools import combinations_with_replacement as h
def counsel(status):
    print(status)
    return -1

def solution(k, n, reqs):
    global answer
    answer = 100*len(reqs)
    
    if n-k==0:
        status = {}
        for i in range(1, k+1):
            status[i] = 1
        return min(answer, counsel(status))
    
    for case in h(range(1, k+1), n-k):
        # 각 유형별로 멘토 인원이 적어도 한 명 이상이어야 합니다.
        status = {}
        for i in range(1, k+1):
            status[i] = 1
            
        for c in case:
            status[c] += 1
        answer = min(answer, counsel(status))
    return answer