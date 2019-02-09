# https://code.google.com/codejam/contest/4374486/dashboard#s=p0
import sys

def main(case):
    N = int(sys.stdin.readline())
    AB = list(map(int, sys.stdin.readline().split(' ')))
    P = int(sys.stdin.readline())
    Ci = []
    for _ in range(P):
        Ci.append(int(sys.stdin.readline()))
    
    Clist = []
    for C in Ci:
        Clist.append(count(C, AB, N))
    msg = ' '
    for i in Clist:
        msg += str(i)+' '
    
    print('Case #{0}:' .format(case+1), end = '')
    print(msg)

def count(C , AB, N):
    a = 0
    for i in range(N):
        A = AB[i*2]
        B = AB[i*2 + 1]
        if (C >= A and C <= B):
            a = a+1
    return a


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        main(i)
        input()
    
