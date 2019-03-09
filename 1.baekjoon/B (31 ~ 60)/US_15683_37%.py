import sys
import numpy as np

sys.setrecursionlimit(100000)

cctv_list = ['1','2','3','4','5','#']

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 6)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector


arr = []
n, m = input().split()
n, m = int(n), int(m)
for i in range(n):
    arr.append(input().split(' '))  

arr = np.array(arr)
arr = np.pad(arr, 1, pad_with)



def main():
    position = []
    
    for i in range(n+2):
        for j in range(m+2):
            if arr[i][j] == '0' or arr[i][j] == '6':
                continue
            else:
                position.append((arr[i][j],(i,j)))
    position = sorted(position)[::-1]
    print('pos: ', position)
    mini_size(position)

    count = 0
    print(arr,n,m)
    for i in range(n+2):
        for j in range(m+2):
            if arr[i][j] == '0':
                count += 1

    print(count) 


def mini_size(position):
    # 1 은 일직선 2는 좌우 3은 지각 4는 좌우앞 5는 정방향
    for pos in position:
        cctv_num , (i , j) = pos
        arr = cctv(cctv_num, i , j)


def cctv(number , i , j):
    if number == '5':
        up(i , j)
        left(i,j )
        right(i, j )
        down(i, j)

    if number == '4':
        # up_line = (up_find(arr, i, j), 'up')
        # left_line = (left_find(arr, i, j),'left')
        # donw_line = (down_find(arr, i, j),'down')
        # right_line =  (right_find(arr, i, j),'right')
        uldr = [up_find(i, j),left_find(i, j),down_find(i, j),right_find(i, j)]
        mins = min(uldr)
        no_line = uldr.index(mins)
        if no_line == 0:
            left(i, j)
            down(i, j)
            right(i, j)
        elif no_line == 1:
            up(i,j)
            down( i, j)
            right( i, j)
        elif no_line == 2:
            up(i,j)
            right(i, j)
            left(i, j)
        else:
            up(i,j)
            left(i,j)
            down(i,j)
    
    if number == '3' or number == '2':
        uldr = [(up_find( i, j),'up'),
        (left_find( i, j),'left'),
        (down_find(i, j),'down'),
        (right_find(i, j),'right')]
        uldr = sorted(uldr)

        ar2 , ar1 = uldr[2][1], uldr[3][1]
        
        ld = {'up': 4,'left':5,'down':6,'right':7}
        
        if number == '2':
            if ar1 == 'up' or ar1 == 'down':
                up(i, j)
                down( i, j)
            else:
                left(i, j)
                right(i, j)
        else:                               ## cctv 3
            if ar1 == 'up' and ar2 == 'left':
                up(i,j)
                left(i,j)
            elif ar1 == 'up' and ar2 == 'right':
                up(i, j)
                right(i, j)
            elif ar1 == 'right' and ar2 == 'up':
                right(i, j)
                up(i ,j)
            elif ar1 == 'right' and ar2 == 'down':
                right(i, j)
                down(i ,j)
            elif ar1 == 'down' and ar2 == 'left':
                down(i, j)
                left(i ,j)
            elif ar1 == 'down' and ar2 == 'right':
                down(i, j)
                right(i ,j)
            elif ar1 == 'left' and ar2 == 'up':
                left(i, j)
                up(i ,j)
            elif ar1 == 'left' and ar2 == 'down':
                left(i, j)
                down(i ,j)
    print(type(number))
    if number == '1':
        uldr = [up_find(i, j),
        left_find(i, j),
        down_find(i, j),
        right_find(i, j)]
        maxs = max(uldr)
        print(maxs)
        no_line = uldr.index(maxs)
        if no_line == 0:
            up(i,j)
        elif no_line == 1:
            left(i,j)
        elif no_line == 2:
            down(i,j)
        else:
            right(i,j)
        
def up_find(i, j):
    if arr[i][j] == '0':
        return up_find(i -1, j) + 1
    elif arr[i][j] in cctv_list:
        return up_find(i -1, j)
    else:
        return 0

def left_find(i, j):
    if arr[i][j] == '0':
        return left_find(i , j - 1) + 1
    elif arr[i][j] in cctv_list:
        return left_find(i , j - 1)
    else:
        return 0
    

def right_find(i, j):
    if arr[i][j] == '0':
        return right_find(i , j + 1) + 1
    elif arr[i][j] in cctv_list:
        return right_find(i , j + 1)
    else:
        return 0


def down_find(i, j):
    if arr[i][j] == '0':
        return down_find(i + 1, j) + 1
    elif arr[i][j] in cctv_list:
        return down_find(i + 1, j)
    else:
        return 0
        


def up(i, j): # i - 1 , j
    if arr[i][j] == '0':
        arr[i][j] = '#'
        up(i - 1, j)
    elif arr[i][j] in cctv_list:
        up(i - 1, j)
    else:
        return

def left(i, j): # i , j -1 
    if arr[i][j] == '0':
        arr[i][j] = '#'
        left(i , j - 1)
    elif arr[i][j] in cctv_list:
        left(i , j - 1)
    else:
        return

def right(i, j): # i, j + 1
    if arr[i][j] == '0':
        arr[i][j] = '#'
        right(i , j + 1)
    elif arr[i][j] in cctv_list:
        right(i , j + 1)
    else:
        return
def down(i, j): # i + 1 , j
    if arr[i][j] == '0':
        arr[i][j] = '#'
        down(i + 1, j)
    elif arr[i][j] in cctv_list:
        down(i + 1, j)
    else:
        return

if __name__ == "__main__":
    main()