from sys import stdin
import collections
MIS = lambda : list(map(int,stdin.readline().split()))

q = collections.deque()

def fake():
    path = []
    selected = []
    unselected = b_list[1:]
    arrow = []
    cur = b_list[0] # (1,1)
    while(1):
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
            arrow.append(str(cur)+'->'+str(nextpos))
        else:
            unselected.remove(nextpos)
            selected.append(nextpos)
            arrow.append(str(nextcur)+'->'+str(nextpos))
        cur = nextcur
    print(arrow)

def getcost(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

if __name__ == "__main__":
    N = int(stdin.readline())
    b_list = [MIS() for i in range(N)]
    print(b_list)
    fake()
    
