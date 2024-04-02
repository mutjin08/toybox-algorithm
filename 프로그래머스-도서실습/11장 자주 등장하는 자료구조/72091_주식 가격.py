def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        temp = 0
        for j in range(i+1, n):
            temp += 1 #주의
            if prices[i] > prices[j]:
                break
        answer.append(temp)
    return answer