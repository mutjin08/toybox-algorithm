def solution(s):
    answer = []
    idx = 0
    for c in s:
        if c==" ":
            answer.append(" ")
            idx = 0
            continue
        
        if idx%2!=0:
            answer.append(c.lower())
        else:
            answer.append(c.upper())
        idx += 1
            
    return "".join(answer)