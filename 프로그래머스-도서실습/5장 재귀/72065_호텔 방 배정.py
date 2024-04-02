# recursion limit
# 새로 answer 배열을 만드는 것 대신 emptyPositions 딕셔너리를 사용
import sys
sys.setrecursionlimit(200000)

def findEmpty(wantRoom, emptyPositions):
    # 빈방
    if wantRoom not in emptyPositions:
        emptyPositions[wantRoom] = wantRoom+1
        return wantRoom
    
    # 찬방
    emptyRoom = findEmpty(emptyPositions[wantRoom], emptyPositions)
    emptyPositions[wantRoom] = emptyRoom+1 #주의
    return emptyRoom

def solution(k, room_number):
    emptyPositions = {}
    for wantRoom in room_number:
        findEmpty(wantRoom, emptyPositions)
    return list(emptyPositions)