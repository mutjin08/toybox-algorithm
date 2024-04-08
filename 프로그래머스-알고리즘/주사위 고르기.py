from itertools import combinations, product

def compete(aScore, bScore):
    result = [0, 0, 0]
    for a, b in product(aScore, bScore):
        if a>b:
            result[0]+=1
        elif a==b:
            result[1]+=1
        elif a<b:
            result[2]+=1
    return result

def roll(aDice):
    result = []
    for case in product(*aDice):
        result.append(sum(case))
    return result
    
    
def solution(dice):
    n = len(dice)
    maxResult = [0, 0, 0]
    for aIndex in combinations(range(n), n//2):
        aIndex = list(aIndex)
        bIndex = []
        for x in range(n):
            if x not in aIndex:
                bIndex.append(x)
        
        aDice, bDice = [dice[i] for i in aIndex], [dice[i] for i in bIndex]
        aScore, bScore = roll(aDice), roll(bDice)
        
        nowResult = compete(aScore, bScore)
        if maxResult[0] < nowResult[0]:
            maxResult = nowResult
            answer = [i+1 for i in aIndex]
    return answer
        