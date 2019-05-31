from sys import stdin
import math

MIS = lambda : stdin.readline().split()

def fake():
    if S == E:
        print(1)
    else:
        flag = True
        i = 0
        while(S + i > E - i):
            if flag:
                if visited[S+i][E-i] == 0:
                    print(1)
                    return
                else:
                    if value[S+i] == value[E-i]:
                        i += 1
                        continue
                    else:
                        flag = False
                    break
            else:
                break
        
        if flag:
            i = 0
            while(S+i < E-i):
                visited[S+i][E-i] = 1
                i = i+1
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    N = int(stdin.readline())
    value = '0' + "".join(list(MIS())) # '1213121'
    M = int(stdin.readline())
    Mlist = [list(map(int,MIS())) for _ in range(M)]
    visited = [[0 for _ in range(2001)] for _ in range(2001)]
    for S, E in Mlist:
        fake()
        
    

