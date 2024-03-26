def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    answer = -1
    while left <= right:
        mid = (left+right)//2
        
        prev_rock = 0
        remove = 0
        for now_rock in rocks:
            if now_rock - prev_rock < mid:
                remove += 1
                if remove > n:
                    break
            else:
                prev_rock = now_rock
                    
        if remove > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer