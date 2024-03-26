def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    
    while left <= right:
        total = 0
        mid = (left+right)//2
        
        for time in times:
            total += mid//time
            if total >= n:
                break
            
        if total >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer