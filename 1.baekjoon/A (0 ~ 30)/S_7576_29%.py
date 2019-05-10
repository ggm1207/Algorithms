import sys
import collections
import queue


MIS = lambda : map(int,sys.stdin.readline().split())
q = collections.deque()

def bfs():
    cnt = 0
    for y in range(m):
        for x in range(n):
            if arr[y][x] == 1:
                q.append((y,x,cnt))
    while(1):
        if not len(q):
            break
        y,x,cnt = q.popleft()
        # print(y,x,cnt)
        if (0 <= y+1 < m) and (0 <= x < n):
            if arr[y+1][x] == 0:
                arr[y+1][x] = 1
                q.append((y+1,x,cnt+1))
        if (0 <= y-1 < m) and (0 <= x < n):
            if arr[y-1][x] == 0:
                arr[y-1][x] = 1
                q.append((y-1,x,cnt+1))
        if (0 <= y < m) and (0 <= x+1 < n):
            if arr[y][x+1] == 0:
                arr[y][x+1] = 1
                q.append((y,x+1,cnt+1))
        if (0 <= y < m) and (0 <= x-1 < n):
            if arr[y][x-1] == 0:
                arr[y][x-1] = 1
                q.append((y,x-1,cnt+1))
    flag = True
    for ar in arr:
        if not all(ar):
            flag = False
    if not flag:
        print(-1)
    else:
        print(cnt)

if __name__ == "__main__":
    n , m = MIS()
    arr = []
    for _ in range(m):
        arr.append(list(MIS()))
    bfs()