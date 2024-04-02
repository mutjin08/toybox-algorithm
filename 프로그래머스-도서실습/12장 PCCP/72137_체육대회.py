from itertools import permutations
def solution(ability):
    n, m = len(ability), len(ability[0]) #people, sport
    
    answer = 0
    for case in permutations(range(n), m):
        answer = max(answer, sum(ability[case[i]][i] for i in range(m)))
    
    return answer