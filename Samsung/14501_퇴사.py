
n = int(input())
schedule = [[0, 0]] #기간, 금액
for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0]*(n+2)

#n일~1일
for i in range(n+1, 0, -1):
    time, pay = schedule[i]

    if i-time <= 0:
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1], dp[i-time]+pay)


print(dp)