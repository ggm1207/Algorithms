import sys
import numpy as np
sys.setrecursionlimit(100000)

def read():
    f = open('./18T.txt','r')
    return f

def init():
    arr = []
    f = read()
    for line in f:
        a = np.array(list(map(int , line.split())))
        arr.append(a)
    return np.array(arr)

def tri(): # 아래 , 오른쪽 아래 
    arr = init()
    num = arr.shape[0]
    # print(arr[1][1])
    maxnum = find_path(arr , 0,0,0, num)
    print(maxnum)

def find_path(arr, i,j, count, maxcount):
    if count == maxcount :
        return 0
    else:
        return max(find_path(arr, i+1,j, count + 1, maxcount) , find_path(arr, i+1, j+1, count +1, maxcount)) + arr[i][j]

if __name__ == "__main__":
    tri()
