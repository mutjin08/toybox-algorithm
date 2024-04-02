def solution(input_string):
    visited = {}
    visited[input_string[0]] = 1
    
    answer = []
    for i in range(1, len(input_string)):
        if input_string[i-1] != input_string[i]:
            if input_string[i] in visited:
                answer.append(input_string[i])
            else:
                visited[input_string[i]] = 1
    
    if len(answer)==0:
        return "N"
    return "".join(sorted(list(set(answer))))