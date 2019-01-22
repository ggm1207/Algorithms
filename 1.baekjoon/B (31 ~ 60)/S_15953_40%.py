import sys


def mod17(a):
    if a > 21 or a == 0:
        return 0
    if a < 2:
        return 5000000
    if a < 4:
        return 3000000
    if a < 7:
        return 2000000
    if a < 11:
        return 500000
    if a < 16:
        return 300000
    else:
        return 100000


def mod18(b):
    if b > 31 or b == 0:
        return 0
    if b < 2:
        return 5120000
    if b < 4:
        return 2560000
    if b < 8:
        return 1280000
    if b < 16:
        return 640000
    else:
        return 320000


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().split(' '))
        print(mod17(a) + mod18(b))
