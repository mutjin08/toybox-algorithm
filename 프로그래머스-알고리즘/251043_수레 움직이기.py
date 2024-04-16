from collections import deque
import copy

def solution(maze):
    m, n = len(maze), len(maze[0])

    # Find start point
    red, blue = [], []
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                red = [i, j]
            elif maze[i][j] == 2:
                blue = [i, j]
    
    # Direction U, D, L, R
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    red_reached, blue_reached = False, False
    vr_, vb_ = [[[False for _ in range(n)] for _ in range(m)] for _ in range(2)]

    # First snapshot
    path = deque()
    path.append(red + blue + [vr_] + [vb_] + [0])

    # Start BFS
    while path:
        rr, rc, br, bc, vr_temp, vb_temp, count = path.popleft()
        
        vr = copy.deepcopy(vr_temp)
        vb = copy.deepcopy(vb_temp)
        vr[rr][rc] = True
        vb[br][bc] = True

        # End condition
        if maze[rr][rc] == 3 and maze[br][bc] == 4: 
            return count
            break
        # Select payload not to move
        else:
            if maze[rr][rc] == 3:
                red_reached = True
                blue_reached = False
            elif maze[br][bc] == 4:
                red_reached = False
                blue_reached = True
            else: 
                red_reached = False
                blue_reached = False

        # seeking path
        for i in range(4):
            if blue_reached:
                r = [rr + dr[i], rc + dc[i]]
                if isBounded(r, m, n):
                    if not (isOverlapped(r, (br, bc)) or isWall(r, maze) or isVisited(r, vr)):
                        path.append([r[0], r[1], br, bc, vr, vb, count + 1])
            elif red_reached:
                b = [br + dr[i], bc + dc[i]]
                if isBounded(b, m, n):
                    if not (isOverlapped(b, (rr, rc)) or isWall(b, maze) or isVisited(b, vb)):
                        path.append([rr, rc, b[0], b[1], vr, vb, count + 1])
            else:
                r = [rr + dr[i], rc + dc[i]]
                if isBounded(r, m, n):
                    if not (isWall(r, maze) or isVisited(r, vr)):
                        for j in range(4):
                            b = [br + dr[j], bc + dc[j]]
                            if isBounded(b, m, n):
                                if not (isOverlapped(r, b) or isSwitched(r, (br, bc), b, (rr, rc)) or isWall(b, maze) or isVisited(b, vb)):
                                    path.append([r[0], r[1], b[0], b[1], vr, vb, count + 1])
    return 0

def isBounded(x, m, n):
    return 0 <= x[0] < m and 0 <= x[1] < n

def isWall(x, map):
    return map[x[0]][x[1]] == 5

def isOverlapped(x, y):
    return (x[0], x[1]) == (y[0], y[1])

def isSwitched(x, y, z, w):
    return (x[0], x[1]) == (y[0], y[1]) and (z[0], z[1]) == (w[0], w[1])

def isVisited(n, v):
    return v[n[0]][n[1]]
