import sys

MIS = lambda : int(sys.stdin.readline())

def fake():
    # 0 : 안 먹고 건너 뛰었을 때
    # 1 : 연속 1번
    # 2 : 연속 2번
    grapevalue[0][0]
    grapevalue[0][1] = grapelist[0]
    grapevalue[0][2]
    for i in range(1,n):
        grape = grapelist[i]
        for prev in grapevalue[i-1]:
            grapevalue[i][0] = max(grapevalue[i-1][2],grapevalue[i-1][1],grapevalue[i-1][0])
            grapevalue[i][1] = grapevalue[i-1][0] + grape
            grapevalue[i][2] = grapevalue[i-1][1] + grape
    
    print(max(grapevalue[n-1]))


if __name__ == "__main__":
    n = MIS()
    grapelist = [MIS() for _ in range(n)]
    grapevalue = [[0 for _ in range(3)] for _ in range(n)]
    fake()