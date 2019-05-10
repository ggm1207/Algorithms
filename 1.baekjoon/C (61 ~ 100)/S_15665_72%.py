import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def dfs(cnt,n, m):
    if cnt == m:
        maxlist.append(tuple(printlist))
        return
    for i in range(1,n+1):
        printlist[cnt] = list1[i-1]
        dfs(cnt+1,n,m) 

if __name__ == "__main__":
    n, m = MIS() # 4 2
    maxlist = []
    list1 =list(MIS())
    printlist = [0 for _ in range(m)]
    dfs(0,n,m)
    maxlist = sorted(list(set(maxlist)))
    for m in maxlist:
        print(" ".join(map(str,m)))

