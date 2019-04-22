from itertools import combinations
from copy import deepcopy
import sys
import queue

sys.setrecursionlimit(100000)
MIS = lambda : map(int, sys.stdin.readline().split())
q = queue.Queue()
# 으아 진짜 못 짠다!!
def laboratory(positions, aarr):
    for x,y in positions:
        aarr[x][y] = '0'
    for x,y in positions:
        if (0 <= x+1 < N) and (0 <= y < N) and (aarr[x+1][y] == 'c' or aarr[x+1][y] == '*'):
            aarr[x+1][y] = 'g'
            q.put((x+1,y,1))
        if (0 <= x-1 < N) and (0 <= y < N) and (aarr[x-1][y] == 'c' or aarr[x-1][y] == '*'):
            aarr[x-1][y] = 'g'
            q.put((x-1,y,1))
        if (0 <= x < N) and (0 <= y+1 < N) and (aarr[x][y+1] == 'c' or aarr[x][y+1] == '*'):
            aarr[x][y+1] = 'g'
            q.put((x,y+1,1))
        if (0 <= x < N) and (0 <= y-1 < N) and (aarr[x][y-1] == 'c' or aarr[x][y-1] == '*'):
            aarr[x][y-1] = 'g'
            q.put((x,y-1,1))
    
    rec(aarr)

    flag = True
    for ar in aarr:
        if 'c' in ar:
            flag = False
    maxs = 0
    if flag:
        for arr in aarr:
            for ar in arr:
                if type(ar) == int:
                    maxs = max(maxs,ar)
    return maxs

# 아 쓰바 잘 못하고 있었네
def rec(aarr):
    # aarr[x][y] == '0'
    while(1):
        if q.qsize():
            x,y,count = q.get()
            # print(x,y,count)
            # for ar in aarr:
            #     for a in ar:
            #         print('%2s' %a, end = '')
            #     print()
            # print()
            rec_arrow(x,y,aarr,count)
        else:
            break


    # rec_arrow(x+1,y,aarr,1)
    # rec_arrow(x-1,y,aarr,1)
    # rec_arrow(x,y+1,aarr,1)
    # rec_arrow(x,y-1,aarr,1)

def rec_arrow(x,y,aarr,count):
    # 범위 검사
    if aarr[x][y] == '*':
        aarr[x][y] = '0'
        if (0 <= x+1 < N) and (0 <= y < N) and aarr[x+1][y] == 'c':
            aarr[x+1][y] = 'g'
            q.put((x+1,y,count+1))
        if (0 <= x-1 < N) and (0 <= y < N) and aarr[x-1][y] == 'c':
            aarr[x-1][y] = 'g'
            q.put((x-1,y,count+1))
        if (0 <= x < N) and (0 <= y+1 < N) and aarr[x][y+1] == 'c':
            aarr[x][y+1] = 'g'
            q.put((x,y+1,count+1))
        if (0 <= x < N) and (0 <= y-1 < N) and aarr[x][y-1] == 'c':
            aarr[x][y-1] = 'g'
            q.put((x,y-1,count+1))
        


    if aarr[x][y] == 'b' or aarr[x][y] == '0':
        return

    if type(aarr[x][y]) == int:
        return

    if aarr[x][y] == 'g':
        aarr[x][y] = count
    
    if (0 <= x+1 < N) and (0 <= y < N) and aarr[x+1][y] == 'c':
        aarr[x+1][y] = 'g'
        q.put((x+1,y,count+1))
    if (0 <= x-1 < N) and (0 <= y < N) and aarr[x-1][y] == 'c':
        aarr[x-1][y] = 'g'
        q.put((x-1,y,count+1))
    if (0 <= x < N) and (0 <= y+1 < N) and aarr[x][y+1] == 'c':
        aarr[x][y+1] = 'g'
        q.put((x,y+1,count+1))
    if (0 <= x < N) and (0 <= y-1 < N) and aarr[x][y-1] == 'c':
        aarr[x][y-1] = 'g'
        q.put((x,y-1,count+1))
 
if __name__ == "__main__":
    N,M = MIS()
    arr = [list(MIS()) for _ in range(N)]
    pos = []

    if all(sum(arr,[])):
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                if not arr[i][j]:
                    arr[i][j] = 'c'
                elif arr[i][j] == 2:
                    pos.append((i,j))
                    arr[i][j] = '*'
                else:
                    arr[i][j] = 'b'
        
        poss = list(combinations(pos,M))
        count = []
        
        for position in poss:
            copy_arr = deepcopy(arr)
            count.append(laboratory(position, copy_arr))
        
        count = list(set(count))
        
        if any(count):
            if 0 in count:
                count.remove(0)
            print(min(count))
        else:
            print(-1)