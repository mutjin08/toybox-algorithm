def parse_plans(plans):
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h*60+m
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x : x[1])
    return plans

def solution(plans):
    answer = []
    
    plans = parse_plans(plans)
    stack = []
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1] # 현재 과제에서 다음 과제까지의 시간 차이
        
        while stack and gap:
            if stack[-1][1] <= gap:
                name, playtime = stack.pop()
                gap -= playtime
                answer.append(name)
            else:
                stack[-1][1] -= gap
                gap = 0
    
    answer.append(plans[-1][0])
    answer.extend([s[0] for s in stack[::-1]])
        
    return answer