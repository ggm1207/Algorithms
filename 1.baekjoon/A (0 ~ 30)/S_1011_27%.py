import sys
import math
MIS = lambda : list(map(int,sys.stdin.readline().split()))

def fake(x,y):
    distance = y - x
    total = 0
    i = 1
    while(1):
        check = i*(i-1) + i # 2 6 12 20
        if distance < check:
            break
        i += 1
    maxnum = i - 1
    total = (i-1)*2 + math.ceil((distance - (i-1)*i)/maxnum)
    print(total)
    


if __name__ == "__main__":
    n = MIS()[0]
    for i in range(n):
        x,y = MIS()
        fake(x,y)