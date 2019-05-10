import sys

MIS = lambda : map(int, sys.stdin.readline().split())

def fake():
    toto = (x1 - x2)**2 + (y1 - y2)**2
    r = (r1 + r2)**2
    if toto == 0:
        if r1 == r2:
            print(-1)
            return
        else:
            print(0)
            return

    if toto > r:
        print(0)
    elif toto == r:
        print(1)
    else:
        print(2)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = MIS()
        fake()
    