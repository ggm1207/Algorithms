import sys
import copy
MIS = lambda : int(sys.stdin.readline())

def fake(num, list1):
    if num - 3 >= 0:
        nl = copy.copy(list1)
        nl.append(num-3)
        fake(num-3,nl)
    if num - 2 >= 0:
        nl = copy.copy(list1)
        nl.append(num-2)
        fake(num-2,nl)
    if num - 1 >= 0:
        nl = copy.copy(list1)
        nl.append(num-1)
        fake(num-1,nl)
    if num == 0:
        lists.append(list1)
    


        


if __name__ == "__main__":
    T = MIS()
    lists = []
    for _ in range(T):
        num = MIS()
        fake(num ,[num])
    nl = []
    for ee in lists:
        nl.append(set(ee))
    print(nl)
    print(set(nl))