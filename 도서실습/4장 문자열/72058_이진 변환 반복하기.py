def convert(x):
    answer = ""
    while x>0:
        answer = str(x%2)+answer
        x //= 2
    return answer

def solution(s):
    answer = [0, 0]
    
    x = s
    while x!="1":
        answer[0]+=1
        
        answer[1]+=len(x)
        x = x.replace("0","")
        answer[1]-=len(x)
        
        c = len(x)
        x = convert(c)
    
    return answer