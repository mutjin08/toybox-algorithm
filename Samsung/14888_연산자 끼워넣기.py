def dfs(add, sub, mul, div, total, depth):
    if depth == n:
        minResult = min(minResult, total)
        maxResult = max(maxResult, total)
        return

    if add:
        dfs(add-1, sub, mul, div, total+numbers[depth], depth+1)
    if sub:
        dfs(add, sub-1, mul, div, total-numbers[depth], depth+1)
    if mul:
        dfs(add, sub, mul-1, div, total*numbers[depth], depth+1)
    if div:
        dfs(add, sub, mul, div-1, total//numbers[depth], depth+1)


n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

minResult, maxResult = int(10e9), -int(10e9)

dfs(operators[0], operators[1], operators[2], operators[3], numbers[0], 1)

print(minResult, maxResult)