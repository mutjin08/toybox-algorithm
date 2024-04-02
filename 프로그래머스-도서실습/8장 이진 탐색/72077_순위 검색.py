from itertools import product
from bisect import bisect_left

"""def bisect_left(arr, target):
    arr.sort()
    left, right = 0, len(arr)
    while left<right:
        mid = (left+right)//2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left"""

def solution(info, query):
    log = {}
    for i in info:
        i = i.split()
        score = int(i.pop())
        
        for key in product([i[0],"-"], [i[1],"-"], [i[2],"-"], [i[3],"-"]):
            key = "".join(key)
            if key not in log:
                log[key] = []
            log[key].append(score)
    
    for value in log.values():
        value.sort()
    
    answer = []
    for q in query:
        q = q.split(" ")
        score = int(q.pop())
        key = "".join(q[::2])
        if key not in log:
            answer.append(0)
        else:
            answer.append(len(log[key])-bisect_left(log[key],score))
    return answer