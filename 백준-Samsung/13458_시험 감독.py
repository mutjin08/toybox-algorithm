n = int(input())
alist = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for a in alist:
    answer+=1 #총감독관
    if b >= a:
        continue

    a -= b
    if a%c==0:
        answer += a//c
    else:
        answer += a//c+1

print(answer)    