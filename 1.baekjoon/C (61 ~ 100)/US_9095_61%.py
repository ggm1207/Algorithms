import sys
sys.setrecursionlimit(1000000)

def dfs(sums,i):
    if sums == n:
        return True
    elif sums > n:
        return dfs(sums-i,i+1)
    else:
        dfs(sums+i,i)
    

def add123():
    cnt = 0
    for i in range(1,4):
        sums = 0
        if dfs(sums,i):
            cnt += 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum(list1[n-1][1:n]))

    