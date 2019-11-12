"""기둥과 보 설치 (https://programmers.co.kr/learn/courses/30/lessons/60061)
입출력 예
n	build_frame	                                            result
5	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
    [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	            [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
5	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],
    [2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	    [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다..!
"""

from itertools import permutations
import random

def solution(n, build_frame):
    build_frame = build_frame[::-1]
    answer = []
    
    installed = [[0 for _ in range(n+1)] for _ in range(n+1)]

    PILLAR = 1 # 기둥
    FLOOR = 2 # 보 ?자기
    INSTALL = 1
    DELETE = 0

    def pillar_install(X, Y):
        if Y == 0:
            return True
        return installed[X][Y-1] == PILLAR or installed[X - 1][Y] == FLOOR

    def floor_install(X, Y):
        if X == 0:
            return installed[X][Y-1] == PILLAR
        if X == n - 1:
            return installed[X + 1][Y - 1] == PILLAR
        return (installed[X-1][Y] == FLOOR and installed[X + 1][Y] == FLOOR) or installed[X][Y-1] == PILLAR or installed[X+1][Y-1] == PILLAR

    def pillar_delete(X, Y):
        temp = installed[X][Y]
        installed[X][Y] = 0
        flag = True
        around_xy = set(permutations([1,1,-1,-1,0],2))
        for AX, AY in around_xy:
            AX, AY = X + AX, Y + AY
            if not (0 <= AX <= n and 0 <= AY <= n):
                continue
            if installed[AX][AY] == PILLAR:
                flag = pillar_install(AX, AY)
            elif installed[AX][AY] == FLOOR:
                flag = floor_install(AX, AY)
            if not flag:
                installed[X][Y] = temp
                break
        return flag

    def floor_delete(X, Y):
        temp = installed[X][Y]
        installed[X][Y] = 0
        flag = True
        around_xy = set(permutations([1,1,-1,-1,0],2))
        for AX, AY in around_xy:
            AX, AY = X + AX, Y + AY
            if not (0 <= AX <= n and 0 <= AY <= n):
                continue
            if installed[AX][AY] == PILLAR:
                flag = pillar_install(AX, AY)
            elif installed[AX][AY] == FLOOR:
                flag = floor_install(AX, AY)
            if not flag:
                installed[X][Y] = temp
                break
        return flag
    
    
    while(build_frame):
        X, Y, A, B = build_frame.pop()
        flag = False
        if B:
            if A + 1 == FLOOR:
                flag = floor_install(X, Y)
            else:
                flag = pillar_install(X, Y)
        else:
            if A + 1 == FLOOR:
                flag = floor_delete(X, Y)
            else:
                flag = pillar_delete(X, Y)
        
        if flag and B == INSTALL:
            installed[X][Y] = A + 1
            answer.append([X,Y,A])
        elif flag and B == DELETE:
            installed[X][Y] = 0
            answer.remove([X,Y,A])

    return sorted(answer, key = lambda x : (x[0],x[1],x[2]))

if __name__ == "__main__":
    n = 5
    # build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    # build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    build_frame = [[random.randint(0,5),random.randint(0,5),random.randint(0,1),random.randint(0,1)] for _ in range(1000)]
    build_frame = build_frame[::-1]
    answer = []
    
    installed = [[0 for _ in range(n+1)] for _ in range(n+1)]

    PILLAR = 1 # 기둥
    FLOOR = 2 # 보 ?자기
    INSTALL = 1
    DELETE = 0

    def pillar_install(X, Y):
        if Y == 0:
            return True
        return installed[X][Y-1] == PILLAR or installed[X - 1][Y] == FLOOR

    def floor_install(X, Y):
        if X == 0:
            return installed[X][Y-1] == PILLAR
        if X == n - 1:
            return installed[X + 1][Y - 1] == PILLAR
            
        return (installed[X-1][Y] == FLOOR and installed[X + 1][Y] == FLOOR) or installed[X][Y-1] == PILLAR or installed[X+1][Y-1] == PILLAR

    def pillar_delete(X, Y):
        temp = installed[X][Y]
        installed[X][Y] = 0
        flag = True
        around_xy = set(permutations([1,1,-1,-1,0],2))
        for AX, AY in around_xy:
            AX, AY = X + AX, Y + AY
            if not (0 <= AX <= n and 0 <= AY <= n):
                continue
            if installed[AX][AY] == PILLAR:
                flag = pillar_install(AX, AY)
            elif installed[AX][AY] == FLOOR:
                flag = floor_install(AX, AY)
            if not flag:
                installed[X][Y] = temp
                break
        return flag

    def floor_delete(X, Y):
        temp = installed[X][Y]
        installed[X][Y] = 0
        flag = True
        around_xy = set(permutations([1,1,-1,-1,0],2))
        for AX, AY in around_xy:
            AX, AY = X + AX, Y + AY
            if not (0 <= AX <= n and 0 <= AY <= n):
                continue
            if installed[AX][AY] == PILLAR:
                flag = pillar_install(AX, AY)
            elif installed[AX][AY] == FLOOR:
                flag = floor_install(AX, AY)
            if not flag:
                installed[X][Y] = temp
                break
        return flag
    
    
    while(build_frame):
        X, Y, A, B = build_frame.pop()
        print(X, Y, A, B)
        flag = False
        if B:
            if A + 1 == FLOOR:
                flag = floor_install(X, Y)
            else:
                flag = pillar_install(X, Y)
        else:
            if A + 1 == FLOOR:
                flag = floor_delete(X, Y)
            else:
                flag = pillar_delete(X, Y)
        
        if flag and B == INSTALL:
            installed[X][Y] = A + 1
            answer.append([X,Y,A])
        elif flag and B == DELETE:
            installed[X][Y] = 0
            answer.remove([X,Y,A])
            

    print(sorted(answer, key = lambda x : (x[0],x[1],x[2])))