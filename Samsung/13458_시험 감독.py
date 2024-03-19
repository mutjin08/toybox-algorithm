from math import ceil
n = int(input())
arr = list(map(int, input().split())) #각 시험장의 응시자수
b, c = list(map(int, input().split())) #총감, 부감

answer = 0
for i in range(n):
    answer += 1
    if arr[i]<=b:
        continue
    arr[i] -= b
    answer += ceil(arr[i]/c)
print(answer)