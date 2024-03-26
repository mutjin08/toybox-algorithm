def solution(arr1, arr2):
    answer = []
    for a in arr1:
        temp = []
        for b in zip(*arr2):
            temp.append(sum(i*j for i, j in zip(a, b)))
        answer.append(temp)
    return answer