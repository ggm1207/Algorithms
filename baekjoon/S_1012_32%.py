import sys
sys.setrecursionlimit(100000)

position = []


def DFS_Cabbage():
    _, _, K = list(map(int, sys.stdin.readline().split(' ')))

    for _ in range(K):
        x, y = list(map(int, sys.stdin.readline().split(' ')))
        position.append((x, y))
    count = 0
    while(1):
        if position:
            count += 1
            a = position.pop()
            DFS(a)  # a is tuple..
        else:
            break
    print(count)

# method 1pop , 1count


def DFS(x):  # x is a position & tuple
    a, b = x
    if (a+1, b) in position:  # right
        position.remove((a+1, b))
        DFS((a+1, b))
    if (a, b+1) in position:  # up
        position.remove((a, b+1))
        DFS((a, b+1))
    if (a-1, b) in position:  # down
        position.remove((a-1, b))
        DFS((a-1, b))
    if (a, b-1) in position:  # left
        position.remove((a, b-1))
        DFS((a, b-1))


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        DFS_Cabbage()
