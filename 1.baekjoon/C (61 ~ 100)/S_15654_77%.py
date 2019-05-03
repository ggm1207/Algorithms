import sys
import copy
MIS = lambda : map(int,sys.stdin.readline().split())

def permutation(list1, maxnum, cnt):
    if cnt > maxnum:
        print(" ".join(printlist))
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
    list1 = sorted(list(MIS()))
    printlist = [0 for _ in range(m)]
    permutation(list1, m, 1)

