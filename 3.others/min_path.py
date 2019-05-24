from sys import stdin
import collections
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

MIS = lambda : list(map(int,stdin.readline().split()))

q = collections.deque()

def fake():
    path = []
    selected = []
    unselected = b_list[1:]
    arrow = []
    cur = b_list[0] # (1,1)
    process = 0
    while(1):
        if process % 100:
            process += 1
        else:
            process += 1
            print(len(unselected), end = '\r')
            
        if not unselected:
            break

        minpath = 1000000
        for i, pos in enumerate(unselected):
            value = getcost(cur,pos)
            if minpath > value:
                minpath = value
                nextpos = pos

        nextcur = cur
        for i, pos in enumerate(selected):
            value = getcost(nextpos, pos)
            if value < minpath:
                minpath = value
                nextcur = pos

        if nextcur == cur:
            unselected.remove(nextpos)
            selected.append(nextpos)
            arrow.append((cur,nextpos))
        else:
            unselected.remove(nextpos)
            selected.append(nextpos)
            arrow.append((nextcur,nextpos))
        cur = nextcur

    show(arrow)

def getcost(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def show(listdata):
    x_list = []
    y_list = []

    for cur, nex in listdata:
        x1, y1 = cur
        x2, y2 = nex
        x_list.append((x1,x2))
        y_list.append((y1,y2))

    # plt.plot([3,4],[3,5])
    #(3,3) -> (4,5)
    for i in range(len(x_list)):
        plt.plot(x_list[i],y_list[i])

    plt.show()

if __name__ == "__main__":
    N = int(stdin.readline())
    b_list = [[random.random(),random.random()] for i in tqdm(range(N))]
    fake()
    
