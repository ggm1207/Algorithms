import sys
import string

MIS = lambda : sys.stdin.readline().split()

def ctoi(c):
    if c <= 'Z':
        return int(c) - int('A')
    return int(c) - int('A')

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    c = [[0 for i in range(52)] for i in range(52)]
    f = [[0 for i in range(52)] for i in range(52)]
    for i in range(N):
        u, v, w = MIS()
        c[ctoi(u)][ctoi(v)] = w
        f[ctoi(u)][ctoi(v)] = w
    
    for ch in c:
        print(ch)
