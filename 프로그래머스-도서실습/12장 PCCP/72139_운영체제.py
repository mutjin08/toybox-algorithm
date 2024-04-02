from heapq import heappush, heappop
def solution(program):
    answer = [0]*11
    
    program.sort(key = lambda x : (x[1],x[0]))
    heap = []
    
    time = 0
    while program or heap:
        while program and program[0][1] <= time:
            heappush(heap, program.pop(0))
            
        if program and not heap:
            time = program[0][1]
            heappush(heap, program.pop(0))

        target = heappop(heap)
        answer[target[0]] += time - target[1]
        time += target[2]
        
    answer[0] = time
    return answer