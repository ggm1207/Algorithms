import numpy as np
import sys

sys.setrecursionlimit(100000)


def read():
    f = open('./11T.txt','r')
    return f
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector

def problem():
    f = read()
    arr = []
    for line in f:
        arr.append(list(map(int , line.split())))
    arr = np.array(arr)
    arr = np.pad(arr, 1, pad_with)
    maxlists = []
    for i in range(1,21):
        for j in range(1,21):
            a = [mul1(arr,i,j,0),mul2(arr,i,j,0),mul3(arr,i,j,0),mul4(arr,i,j,0)]
            maxlists.append(a)
    maxlists = sum(maxlists, [])
    print(max(maxlists))
            

def mul1(arr, i, j, n): # 밑으로 내려가는거
    if arr[i][j] == 0:
        return 0
    if n == 4:
        return 1
    else:
        return mul1(arr, i - 1 ,j , n + 1) * arr[i][j]

def mul2(arr, i, j, n): # 왼쪽 아래
    if arr[i][j] == 0:
        return 0
    if n == 4:
        return 1
    else:
        return mul2(arr, i - 1 ,j - 1 , n + 1) * arr[i][j]

def mul3(arr, i, j, n): # 오른쪽 아래
    if arr[i][j] == 0:
        return 0
    if n == 4:
        return 1
    else:
        return mul3(arr, i - 1 ,j + 1, n + 1) * arr[i][j]

def mul4(arr, i, j, n): # 오른쪽
    if arr[i][j] == 0:
        return 0
    if n == 4:
        return 1
    else:
        return mul4(arr, i  ,j + 1, n + 1) * arr[i][j]

if __name__ == "__main__":
    problem()