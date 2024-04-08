from itertools import combinations, product
def compete(aScores, bScores):
    answer = 0
    aScores.sort()
    bScores.sort()
    
    for a in aScores:
        left, right = 0, len(bScores)-1
        while left <= right:
            mid = (left+right)//2
            
            if bScores[mid] < a:
                answer+= mid - left + 1
                left = mid+1
            else:
                right = mid-1
                
    return answer

def getScore(dices):
    scores = []
    for case in product(*dices):
        scores.append(sum(case))
    return scores
def solution(dice):
    n = len(dice)
    answer, maxCount = 0, 0
    for aDiceIdx in combinations(range(n), n//2):
        aDices, bDices = [], []
        for i in range(n):
            if i in aDiceIdx:
                aDices.append(dice[i])
            else:
                bDices.append(dice[i])
        aScores, bScores = getScore(aDices), getScore(bDices)
        winCount = compete(aScores, bScores)
        if maxCount < winCount:
            maxCount = winCount
            answer = aDiceIdx
    return [i+1 for i in answer]
    