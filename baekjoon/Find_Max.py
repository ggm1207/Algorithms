''' 9 x 9 배열을 받고 최대값과 인덱스를 리턴. '''

import numpy as np

def Find(arr):
    maxs = arr.max()
    print(maxs)
    a = np.where(arr == maxs)
    print(a[0][0] , end = ' ') ; print(a[1][0])

if __name__ == "__main__":
    arr = np.zeros((9,9))
    for i in range(9):
        arr[i] = input().split()
    Find(arr)
