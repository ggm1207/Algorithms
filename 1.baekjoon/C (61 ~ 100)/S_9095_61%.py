import sys
sys.setrecursionlimit(1000000)


def dp(num):
    if num >= 3:
        return dp(num-1) + dp(num-2) + dp(num-3)
    elif num > 0:
        return num
    else:
        return 1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(dp(n))