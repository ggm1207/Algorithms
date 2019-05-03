import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def dfs(cnt,n, m):
    if cnt == m:
        print(" ".join(printlist))
        return
    if cnt - 1 < 0 :
        a = 1
    else:
        a = int(printlist[cnt-1])
    for i in range(a,n+1):
        printlist[cnt] = str(i)
        dfs(cnt+1,n,m) 

if __name__ == "__main__":
    n, m = MIS() # 4 2
    printlist = [1 for _ in range(m)]
    dfs(0,n,m)

