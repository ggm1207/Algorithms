import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def dfs(cnt,n, m):
    if cnt == m:
        print(" ".join(map(str,printlist)))
        return
    if cnt - 1 < 0 :
        a = list1[0]
    else:
        a = printlist[cnt-1]
    # print(list1)
    # print(list1.index(1))
    for i in range(list1.index(a),n):
        printlist[cnt] = list1[i]
        dfs(cnt+1,n,m) 

if __name__ == "__main__":
    n, m = MIS() # 4 2
    list1 = sorted(list(MIS()))
    printlist = [1 for _ in range(m)]
    dfs(0,n,m)

