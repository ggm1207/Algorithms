import sys
import heapq
import copy

MIS = lambda : map(int, sys.stdin.readline().split())

q = []
nextPos = [(0,1),(0,-1),(1,0),(-1,0)]
visited = {}
# push -> var
# q 에서 꺼내오고
# 가능한 var 계산후 q push
# 
def fake(): # inp : int
    flag = True
    a = str(inp)[0]
    heapq.heappush(q,(0 + getCount(str(inp)),inp))
    i = 0
    while(q):
        count, posvalue = heapq.heappop(q)
        # print( count, posvalue)
        visited[posvalue] = count
        
        depth = count - getCount(str(posvalue))
        if var1 == posvalue:
            print(depth)
            return
        getPosValue(depth, posvalue)
    print(-1)
        # if i == 10:
        #     break
        # i += 1


def getCount(posvalue): # posvalue : str
    return sum(list(map(lambda x, y : x == y,var,posvalue)))
    
def getPosValue(depth, posvalue): # push next q
    posvalue = list(str(posvalue))
    index = posvalue.index('9')
    nextList = []
    a, b = numtopos(index)
    for x, y in nextPos:
        nextList.append(postonum((a + x,b + y)))
    nextList = list(filter(lambda x : 0 <= x < 9, nextList))
    for nextIndex in nextList:
        tmp = copy.copy(posvalue)
        tmp[index], tmp[nextIndex] = tmp[nextIndex], tmp[index]
        n = (depth + 1 + getCount(tmp), int("".join(tmp)))
        dddd = n[1]
        # print(dddd)
        if dddd in visited:
            if visited[dddd] > n[0]:
                heapq.heappush(q,n)
        else:
            visited[dddd] = n[0]
            heapq.heappush(q,n)
    
def numtopos(num):
    return divmod(num-1,3)
    
def postonum(pos):
    return pos[0]*3 + pos[1] + 1


if __name__ == "__main__":
    var1 = 123456789
    var = '123456789'
    inp = []
    for i in range(3):
        inp += sys.stdin.readline().split()
    inp[inp.index('0')] = '9'
    inp = int("".join(inp))
    fake()