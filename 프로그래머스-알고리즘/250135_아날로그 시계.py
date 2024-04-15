# 초침의 단위를 중심으로 파악해 보자
def solution(h1, m1, s1, h2, m2, s2):
    h, m, s = h1, m1, s2
    while True:
        s+=1
        if s>=60:
            s=0
            m+=1
        if m>=60:
            m=0
            h+=1
        print(h, m, s)
        if h==h2 and m==m2 and s==s2:
            break

solution(0, 5, 30, 0, 7, 0)