def solution(picks, minerals):
    answer = 0
    sum =0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals)>sum:
        minerals = minerals[:num]
    
    #광물들을 조사한다.
    new_minerals =[[0,0,0] for _ in range((len(minerals) //5 +1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
