def solution(temperature, t1, t2, a, b, onboard):
    min_temp, max_temp = t1, t2
    
    # dp[temp][t] = time t, indoor temperature is (temp+10) degrees
    # minimum power consumption to create this situation
    dp = [[1e9] * 51 for _ in range(1001)]
    
    # Initialization (t=0)
    dp[0][temperature + 10] = 0
    
    for t, is_onboard in enumerate(onboard[1:], 1):
        # Consider only the situation where the passenger is on board
        # and mintemp <= temp <= maxtemp
        if is_onboard:
            min_temp_to_consider = min_temp
            max_temp_to_consider = max_temp + 1
        else:
            min_temp_to_consider = -10
            max_temp_to_consider = 40 + 1
            
        for temp in range(min_temp_to_consider, max_temp_to_consider):
            if temp == temperature:
                candidates = [dp[t - 1][temp + 10]]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])
                    
                dp[t][temp + 10] = min(candidates)
                
            elif temp > temperature:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10] + a)
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10])
                    
                dp[t][temp + 10] = min(candidates)
            else:
                candidates = [dp[t - 1][temp + 10] + b]
                if temp + 10 != 0:
                    candidates.append(dp[t - 1][temp - 1 + 10])
                if temp + 10 != 50:
                    candidates.append(dp[t - 1][temp + 1 + 10] + a)
                    
                dp[t][temp + 10] = min(candidates)

    answer = min(dp[len(onboard) - 1])
    return answer
