import sys

sys.setrecursionlimit(100000)

cctv_list = ['1','2','3','4','5','#']

class CCTV():
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.arr = self.make_arr()
        # self.check_arr()
        self.position = self.extract_position()

    def make_arr(self):
        arr = []
        for i in range(self.n+2):
            arr.append(['6' for i in range(self.m+2)])
        ori = []
        for i in range(self.n):
            ori.append(input().split(' '))
        i, j = 1,1
        for ri in ori:
            j = 1
            for r in ri:
                arr[i][j] = r
                j += 1
            i += 1
        return arr  
    
    def check_arr(self):
        for array in self.arr:
            print(array)
    
    def extract_position(self):
        position = []
        for i in range(self.n+2):
            for j in range(self.m+2):
                if self.arr[i][j] == '0' or self.arr[i][j] == '6':
                    continue
                else:
                    position.append((self.arr[i][j],(i,j)))
        position = sorted(position)[::-1]
        print('pos: ', position)
        return position

    def solve_cctv(self):


if __name__ == "__main__":
    n, m = list(map(int ,input().split()))
    CCTV(n,m)
    