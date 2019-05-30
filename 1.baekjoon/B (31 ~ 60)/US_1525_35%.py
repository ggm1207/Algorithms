import sys
import heapq
import copy

MIS = lambda : map(int, sys.stdin.readline().split())

q = []
nextPos = [(0,1),(0,-1),(1,0),(-1,0)]

def fake():
    x , y = nums[0]
    heqppush(q, (0, nums[0]))
    maxnum = 0
    while(1):
        depth, x,y = q.heappop()
        nextlist = []
        for a,b in nextPos:
            if (x+a,y+b) in list(nums.values()):
                nextlist.append((x+a,y+b))
        
        for poss in nextlist: # 0 근처 위치
            heqppush(depth ,poss)
            

def check():
    count = 0
    for i in range(3):
        for j in range(3):
            if 3*i+j+1 < 9:    
                if (i,j) == nums[3*i+j+1]:
                    count += 1
            else:
                if (2,2) == nums[0]:
                    count += 1
    return count



if __name__ == "__main__":
    var = [[1,2,3],[4,5,6],[7,8,0]]
    nums = {}
    pos = {}
    for i in range(3):
        a, b, c = MIS()
        nums[a] = (i,0)
        nums[b] = (i,1)
        nums[c] = (i,2)
        pos[(i,0)] = a
        pos[(i,1)] = b
        pos[(i,2)] = c

    print(nums)
    print(pos)
    fake()
    print(check())