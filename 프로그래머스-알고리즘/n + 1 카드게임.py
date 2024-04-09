def targetExist(cards):
    global n
    target = n+1
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i] + cards[j] == target:
                return i, j
    return -1, -1

def backtracking(stage, coin, cards, haves):
    global answer
    if len(cards)<2:
        answer = max(answer, stage)
        return
    
    a = cards.pop(0)
    b = cards.pop(0)
    
    # case1
    nHaves = haves
    i, j = targetExist(nHaves)
    if i!=-1:
        nHaves = nHaves[:i]+nHaves[i+1:j]+nHaves[j+1:]
        backtracking(stage+1, coin, cards, nHaves)
    else:
        answer = max(answer, stage)
        return
        
    # case2
    if coin >= 1:
        nHaves = haves+[a]
        i, j = targetExist(nHaves)
        if i!=-1:
            nHaves = nHaves[:i]+nHaves[i+1:j]+nHaves[j+1:]
            backtracking(stage+1, coin-1, cards, nHaves)
        else:
            answer = max(answer, stage)
            return
    
    # case3
    if coin >= 1:
        nHaves = haves+[b]
        i, j = targetExist(nHaves)
        if i!=-1:
            nHaves = nHaves[:i]+nHaves[i+1:j]+nHaves[j+1:]
            backtracking(stage+1, coin-1, cards, nHaves)
        else:
            answer = max(answer, stage)
            return
            
    # case4
    if coin >= 2:
        nHaves = haves+[a, b]
        i, j = targetExist(nHaves)
        if i!=-1:
            nHaves = nHaves[:i]+nHaves[i+1:j]+nHaves[j+1:]
            backtracking(stage+1, coin-2, cards, nHaves)
        else:
            answer = max(answer, stage)
            return
        

def solution(coin, cards):
    global n
    n = len(cards)
    haves = cards[:n//3]
    cards = cards[n//3:]
    
    global answer
    answer = 0
    backtracking(1, coin, cards, haves)
    return answer