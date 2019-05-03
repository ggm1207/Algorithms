import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def permutation(list1, maxnum, cnt):
    if cnt > maxnum:
        maxlist.append(tuple(sorted(printlist)))
        return
    for i , num in enumerate(list1):
        list2 = copy.deepcopy(list1)
        printlist[cnt -1] = str(num)
        # print(i)
        list2.remove(num)
        # print(list2)
        permutation(list2, maxnum, cnt+1)

if __name__ == "__main__":
    n, m = MIS() # 4 2
    printlist = [0 for _ in range(m)]
    maxlist = []
    list1 = [i for i in range(1,n+1)]
    permutation(list1, m, 1)
    # print(maxlist)
    # print(set(maxlist))
    maxlist = sorted(list(set(maxlist)))
    for a in maxlist:
        print(" ".join(a))

