wordList = []
def makeWord(word):
    if len(word)==5:
        return
    for w in "AEIOU":
        wordList.append(word+w)
        makeWord(word+w)
        
def solution(word):
    makeWord("")
    return wordList.index(word)+1