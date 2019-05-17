import sys
import collections

MIS = lambda : sys.stdin.readline()[:-1]

def fake():
    q = collections.deque()
    q.append((0,0,0))
    crushnum = []
    while(1):
        if not len(q):
            break
        y,x,cnt = q.popleft()
        print( y, x, cnt)
        if cnt > n + m:
            break
        
        if visited[y][x]:
            if cnt > min(visited[y][x]):
                continue

        visited[y][x].append(cnt)
        if y == m-1 and x == n-1:
            crushnum.append(cnt)
            continue

        if (0 <= y+1 < m) and (0 <= x < n):
            if arr[y+1][x] == '0':
                q.append((y+1,x,cnt))
            else:
                q.append((y+1,x,cnt+1))
        if (0 <= y-1 < m) and (0 <= x < n):
            if arr[y-1][x] == '0':
                q.append((y-1,x,cnt))
            else:
                q.append((y-1,x,cnt+1))
        if (0 <= y < m) and (0 <= x+1 < n):
            if arr[y][x+1] == '0':
                q.append((y,x+1,cnt))
            else:
                q.append((y,x+1,cnt+1))
        if (0 <= y < m) and (0 <= x-1 < n):
            if arr[y][x-1] == '0':
                q.append((y,x-1,cnt))
            else:
                q.append((y,x-1,cnt+1))
    print(min(crushnum))
# 0, 0 -> N-1,M-1
# '0' : empty room
# '1' : wall
if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    arr = [list(MIS()) for _ in range(m)]
    visited = [[[] for _ in range(n)] for _ in range(m)]
    fake()