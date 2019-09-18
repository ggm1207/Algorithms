# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from sys import stdin
from collections import defaultdict
from itertools import combinations
sys.setrecursionlimit(100000)

MIS = lambda : tuple(map(int, stdin.readline().split()))

def inspect(x,y):
    return -30000 <= x <= 30000 and -30000 <= y <= 30000

def dist(p1, p2):
    return pow(p1[0] - p2[0],2) + pow(p1[1] - p2[1],2)

def _closet_pair(xy_pos, N):
    if N == 2:
        return dist(xy_pos[0], xy_pos[1])
    if N == 3:
        return min(dist(xy_pos[0], xy_pos[1]),dist(xy_pos[1], xy_pos[2]),dist(xy_pos[2], xy_pos[0]))
    d = min(_closet_pair(xy_pos[:int(N/2)], int(N/2)), _closet_pair(xy_pos[int(N/2):], N - int(N/2)))
    
    elif len(xy_pos):


def _main():
    N = int(stdin.readline().rstrip('\n'))
    xy_pos = sorted([MIS() for _ in range(N)])
    d = _closet_pair(xy_pos, N)
    print(d)

if __name__ == "__main__":
	_main()