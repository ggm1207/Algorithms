import sys

MIS = lambda : map(int,sys.stdin.readline().split())
visited = [0 for _ in range(505)]

def dfs(here):
    if visited[here]:
        return False
    visited[here] = 1
    for there in arr[here]:
        if not bMatch[there] or dfs(bMatch[there]):
            bMatch[there] = here
            return True
        
def bmatch():
    global visited
    ret = 0
    for i in range(1,n+1):
        visited = list(map(lambda x : 0, visited))
        if dfs(i):
            ret += 1
    return ret

if __name__ == "__main__":
    n , k = MIS()
    arr = [[] for _ in range(n+1)]
    bMatch = [0 for _ in range(n+1)]
    
    for i in range(k):
        x,y = MIS()
        arr[x].append(y)
        
    print(bmatch())

    