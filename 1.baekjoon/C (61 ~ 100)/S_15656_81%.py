import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def dfs(cnt,n, m):
    if cnt == m:
        print(" ".join(printlist))
        return
    for i in range(0,n):
        printlist[cnt] = str(list1[i])
        dfs(cnt+1,n,m) 

if __name__ == "__main__":
    n, m = MIS() # 4 2
    list1 = list(MIS())
    printlist = [0 for _ in range(m)]
    dfs(0,n,m)

