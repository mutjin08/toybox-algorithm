n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]
for i in range(n):
    time, price = schedule[i]
    for j in range(i+time, n+1):
        if dp[j] < dp[i]+price:
            dp[j] = dp[i]+price

print(dp[n])