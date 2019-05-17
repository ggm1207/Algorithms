def makedicts(j):
    dicts = {}
    for i in range(1,10):
        dicts[i] = j
    dicts[0] = 0
    return dicts

def stair():
    firstlist = makedicts(1)
    for _ in range(N-1):
        firstlist = addnum(firstlist)
    print(sum(firstlist.values()) % 1000000000)

def addnum(firstlist):
    newlist = makedicts(0)
    for i,num in firstlist.items():
        if i == 0:    
            newlist[1] += num % 1000000000
        elif i == 9:
            newlist[8] += num % 1000000000
        else:
            newlist[i-1] += num % 1000000000
            newlist[i+1] += num % 1000000000
    return newlist

if __name__ == "__main__":
    N = int(input())
    stair()