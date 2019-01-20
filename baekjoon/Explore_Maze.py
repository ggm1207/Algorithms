'''정답은 맞는데 쓰레기 알고리즘 이거 쓸바에 안씀.'''
import numpy as np
global n,m
global lists
lists = []

def StartAdventure():
    arr = init_arr()
    Find_Mini(arr,1,1,1)
    print(set(lists))
    print(min(lists))

def Find_Mini(arr, i, j, count):
    if count > (n-2)*(m-2) - (n-3) * ((m-2)/2):
        return

    if i == n-2 and j == m-2:
        lists.append(count)
        return

    if arr[i][j] == 1:
        Find_Mini(arr,i-1,j,count+1)
        Find_Mini(arr,i,j-1,count+1)
        Find_Mini(arr,i+1,j,count+1)
        Find_Mini(arr,i,j+1,count+1)
    else:
        return

def init_arr():
    arr = np.zeros((n,m))
    for i in range(1,n-1):
        arr[i] = [0] + input().split() + [0]
    print(arr)
    return arr



if __name__ == "__main__":
    n , m = input('n,m 을 입력해주세요:').split()
    n , m = int(n) + 2 , int(m) + 2
    StartAdventure()
