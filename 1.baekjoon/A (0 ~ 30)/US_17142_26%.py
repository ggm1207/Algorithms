import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

MIS = lambda : map(int, sys.stdin.readline().split())

q = deque()
N = 0
M = 0

# 0 : empty , 1 : wall, 2 : virus
# 1. 조합으로 활성 바이러스의 경우의 수를 구한다.
# 2. queue 에 처음 활성 바이러스를 집어 넣는다.
# 3. bfs 후 min_cnt = min(min_cnt, count)를 저장한다. 
# 4. bfs 중 cnt > min_cnt 를 넘어서면 종료
# 5. 모든 경우의 수 끝나고 min_cnt 출력

arrow = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    min_cnt = 10000
    virusList = list(combinations(getVirusList(), M))
    
    for virus in virusList: # 경우의 수
        visited = deepcopy(lab)
        max_cnt = 0
        print('*'*40)
        print(virus)
        q = deque()

        for y,x in virus: # 초기 활성 바이러스
            q.append((y,x,0))
            visited[y][x] = -1

        while(q):
            y, x, cnt = q.popleft()
            if cnt > min_cnt:
                # print(cnt, min_cnt)
                # print('break')
                break

            print(y,x, cnt)
            for yc, xc in arrow:
                if 0 <= y + yc < N and 0 <= x + xc < N and visited[y+yc][x+xc] != 1:
                    if visited[y+yc][x+xc] == 2:
                        visited[y+yc][x+xc] = -1
                        q.append((y+yc, x+xc, cnt + 1))
                    if visited[y+yc][x+xc] == 0:
                        visited[y+yc][x+xc] = cnt + 1
                        q.append((y+yc, x+xc, cnt + 1))
            for visit in visited:
                print(visit)
            print()

        min_cnt = min(min_cnt, cnts)
    print(min_cnt)

def getVirusList():
    l = []
    for y in range(N):
        for x in range(N):
            if lab[y][x] == 2:
                l.append((y,x))
    return l
         
if __name__ == "__main__":
    N, M = MIS() # 4 <= N <= 50, 1 <= M <= 10
    lab = [list(MIS()) for _ in range(N)]
    # print(lab)
    bfs()