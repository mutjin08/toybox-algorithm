def solution(s, n):
    answer = []
    for c in s:
        if ord("a")<=ord(c)<=ord("z"):
            c = ord(c)+n
            if c > ord("z"):
                c -= 26
            answer.append(chr(c))
        elif ord("A")<=ord(c)<=ord("Z"):
            c = ord(c)+n
            if c > ord("Z"):
                c -= 26
            answer.append(chr(c))
        else:
            answer.append(" ")
    return "".join(answer)
        