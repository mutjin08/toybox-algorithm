def solution(s):
    answer = [len(s)]
    for cut in range(1, len(s)//2+1):
        compressed = ""
        pattern = s[:cut]
        repeat = 1
        for i in range(cut, len(s)+cut, cut):
            if pattern == s[i:i+cut]:
                repeat += 1
            else:
                if repeat > 1:
                    compressed += str(repeat)+pattern
                else:
                    compressed += pattern
                pattern = s[i:i+cut]
                repeat = 1
        answer.append(len(compressed))
    return min(answer)