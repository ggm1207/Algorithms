import sys
import functools as f

MIS = lambda : map(int,sys.stdin.readline().split())

if __name__ == "__main__":
    n , k = MIS()
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(k):
        x,y = MIS()
        arr[x][y] = 1
        arr[x][0] += 1
        arr[0][y] += 1

    width = f.reduce( lambda x , y: x + 1 if x, arr[0],0)
    print(width)
    