
def solution(progresses, speeds):
    times = []
    for p, s in zip(progresses, speeds):
        time = (100-p)//s
        if (100-p)%s!=0:
            time += 1
        times.append(time)
    times.reverse()
    
    answer = []
    while times:
        unit = times.pop()
        cnt = 1
        while times and times[-1] <= unit:
            times.pop()
            cnt += 1
        answer.append(cnt)
    return answer