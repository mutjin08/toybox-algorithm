def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        temp = []
        for a2 in zip(*arr2):
            temp.append(sum([i*j for i, j in zip(a1, a2)]))
        answer.append(temp)
    return answer