import sys

MIS = lambda : list(map(int,sys.stdin.readline().split()))

N = int(input())
for i in range(N):
    print(sum(MIS()))