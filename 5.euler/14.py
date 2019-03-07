import sys
sys.setrecursionlimit(100000)

def hailstone(n, i):
    if n == 1:
        return i
    else:
        if n % 2 == 0:
            return hailstone(n/2 , i+1)
        else:
            return hailstone(3*n+1, i+1)


if __name__ == "__main__":
    maxnum = 0
    maxcal = 0
    a = 0
    for i in range(1,1000001):
        a = hailstone(i, 1)
        if (a > maxcal):
            maxcal = a
            maxnum = i
    print(maxcal, maxnum)