def solution(k, room_number):
    rooms = [0]*(k+1)
    answer = []
    for x in room_number:
        #빈방
        if not rooms[x]:
            rooms[x] = 1
            answer.append(x)
            continue
        
        #찬방
        for y in range(x+1, k+1):
            if not rooms[y]:
                rooms[y] = 1
                answer.append(y)
                break
    return answer