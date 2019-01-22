import numpy as np



def Fishing():
    global n
    global arr
    n,l,m = map(int ,input().split())
    arr = np.zeros((n+2,n+2))
    for i in range(m):
        x, y = map(int,input().split())
        arr[x][y] = 1
    lxy = []
    for i in range(1 , l//2):
        lxy.append((i , l//2 - i))
    max = 0
    for lx, ly in lxy:
        temp = Fishing_with_net(lx, ly, n)
        if(max < temp):
            max = temp

def Fishing_with_net(lx, ly, n):
    max = 0
    for i in range(1, n - lx + 1):
        for j in range(1, n - ly + 1):
            temp = Check_Fishnum(i,j,lx,ly)
            if max < temp:
                max = temp
    return temp

def Check_Fishnum(i,j,lx,ly):
    count = 0
    for i in range(i,i + lx + 1):
        for j in range(j, j+ly + 1):
            if arr[i][j] == 1:
                count += 1
    return count


if __name__ == "__main__":
    Fishing()
