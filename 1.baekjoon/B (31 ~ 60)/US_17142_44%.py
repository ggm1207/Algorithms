from itertools import combinations
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

MIS = lambda : map(int, sys.stdin.readline().split())

def laboratory(positions, aarr):
    for x,y in positions:
        aarr[x][y] = '0'
    for x,y in positions:
        rec(x,y, aarr)
    maxs = 0
    flag = True
    for ar in aarr:
        if 'c' in ar:
            flag = False
    
    if flag:
        for arr in aarr:
            for ar in arr:
                if type(ar) == int:
                    maxs = max(maxs,ar)
    return maxs

# 아 쓰바 잘 못하고 있었네
def rec(x,y, aarr):
    # aarr[x][y] == '0'
    rec_arrow(x+1,y,aarr,1)
    rec_arrow(x-1,y,aarr,1)
    rec_arrow(x,y+1,aarr,1)
    rec_arrow(x,y-1,aarr,1)

def rec_arrow(x,y,aarr,count):
    # 범위 검사
    if not (0 <= x < N) or not (0 <= y < N):
        return

    if arr[x][y] == 'b' or arr[x][y] == '*':
        return

    if type(aarr[x][y]) == int:
        if aarr[x][y] > count:
            aarr[x][y] = count
        else:
            return

    if aarr[x][y] == 'c':
        aarr[x][y] = count

    rec_arrow(x+1,y,aarr,count+1)
    rec_arrow(x-1,y,aarr,count+1)
    rec_arrow(x,y+1,aarr,count+1)
    rec_arrow(x,y-1,aarr,count+1)

if __name__ == "__main__":
    N,M = MIS()
    arr = [list(MIS()) for _ in range(N)]
    pos = []
    ff = True
    for ar in arr:
        for a in ar:
            if a:
                continue
            else:
                ff = False
                break
    if ff:
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