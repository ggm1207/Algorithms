import sys
import collections

MIS = lambda : sys.stdin.readline()[:-1]

def show():
    for ar in visited:
        print(ar)
def fake():
    q = collections.deque()
    q.append((0,0,0))
    crushnum = []

    while(1):
        if not len(q):
            break

        y,x,cnt = q.popleft()
        # print(y, x, cnt)
        # show()

        if y == m-1 and x == n-1:
            crushnum.append(cnt)
            continue

        if 0 <= y+1 < m and 0 <= x < n:
            if cnt >= visited[y+1][x]:
                pass
            else:
                if arr[y+1][x] == '0':
                    q.append((y+1,x,cnt))
                    visited[y+1][x] = cnt
                else:
                    if cnt+1 < visited[y+1][x]:
                        q.append((y+1,x,cnt+1))
                        visited[y+1][x] = cnt+1
        if 0 <= y-1 < m and 0 <= x < n:
            if cnt >= visited[y-1][x]:
                pass
            else:
                if arr[y-1][x] == '0':
                    q.append((y-1,x,cnt))
                    visited[y-1][x] = cnt
                else:
                    if cnt+1 < visited[y-1][x]:
                        q.append((y-1,x,cnt+1))
                        visited[y-1][x] = cnt+1
        if 0 <= y < m and 0 <= x+1 < n:
            if cnt >= visited[y][x+1]:
                pass
            else:
                if arr[y][x+1] == '0':
                    q.append((y,x+1,cnt))
                    visited[y][x+1] = cnt
                else:
                    if cnt+1 < visited[y][x+1]:
                        q.append((y,x+1,cnt+1))
                        visited[y][x+1] = cnt
        if 0 <= y < m and 0 <= x-1 < n:
            if cnt >= visited[y][x-1]:
                pass
            else:
                if arr[y][x-1] == '0':
                    q.append((y,x-1,cnt))
                    visited[y][x-1] = cnt
                else:
                    if cnt+1 < visited[y][x-1]:
                        q.append((y,x-1,cnt+1))
                        visited[y][x-1] = cnt
    # print(crushnum)
    print(min(crushnum))
# 0, 0 -> N-1,M-1
# '0' : empty room
# '1' : wall
if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    arr = [list(MIS()) for _ in range(m)]
    visited = [[100000000000 for _ in range(n)] for _ in range(m)]
    fake()