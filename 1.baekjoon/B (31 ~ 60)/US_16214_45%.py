import sys
import time
from functools import reduce
sys.setrecursionlimit(10000)
MIS = lambda : map(int, sys.stdin.readline().split())

def fake(n,m):
    a = n
    while(1):
        n1 = (reduce(lambda x, y: x*y ,[n%m for _ in range(a)]))%m
        if n1 == n:
            print(n)
            break
        n = n1

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = MIS()
        fake(n,m)
        