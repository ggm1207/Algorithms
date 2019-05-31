from sys import stdin
from itertools import permutations

MIS = lambda : stdin.readline().rstrip()

def fake():
    number = list(range(10-len(ditvalue),10))
    possible = permutations(number)
    for posss in possible:
        dicts = {}
        for i, pos in enumerate(posss):
            dicts[ditvalue[i]] = pos
        fi(dicts)


def fi(dicts): # return sum
    total = 0
    for sl in sum_list:
        


if __name__ == "__main__":
    n = int(stdin.readline())
    sum_list = [MIS() for _ in range(n)]
    ditvalue = ''
    for al in sum_list:
        ditvalue += al
    ditvalue = list(set(ditvalue))
    fake()
