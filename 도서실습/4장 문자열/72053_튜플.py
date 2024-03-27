def solution(s):
    tuples = []
    for c in s.lstrip("{{").rstrip("}}").split("},{"):
        tuples.append(list(map(int, c.split(","))))
    
    tuples.sort(key = len)
    
    answer = []
    for tup in tuples:
        for x in tup:
            if x not in answer:
                answer.append(x)
    return answer