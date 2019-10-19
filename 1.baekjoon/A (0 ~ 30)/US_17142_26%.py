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

def div_virus(lab, v_y, v_x):
    mask = lab[:]
    prev_v = [(v_y, v_x)]
    count = 0
    while(1):
        next_v = []
        for y, x in prev_v:



        prev_v = next_v 



def fake():
    min_cnt = 10000
    virus_possible = {}
    all_virusList = getVirusList()
    virusList = list(combinations(all_virusList, M))
    # print(all_virusList)
    # print(virusList)
    for v_y, v_x in all_virusList:
        virus_possible[(v_y, v_x)] = div_virus(lab, v_y, v_x)

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
    print(lab)
    fake()