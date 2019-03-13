import sys
import copy

sys.setrecursionlimit(100000)
sys.getrecursionlimit()
cctv_list = ['1','2','3','4','5','#']

class CCTV():
    def __init__(self,n,m, arr):
        self.n = n
        self.m = m
        self.arr = self.make_arr(arr)
        # self.check_arr(self.arr)
        self.position = self.extract_position()
        self.allof = [] # 모든 경우의 수를 저장
        self.solve_cctv()
        # self.check_arr()
        # self.allof = list(set(self.allof))
        # print(self.allof)
        print(min(self.allof))

    def make_arr(self, ori_arr):
        arr = []
        for _ in range(self.n+2):
            arr.append(['6' for _ in range(self.m+2)])
        
        for i in range(self.n):
            arr[i+1][1:self.m+1] = ori_arr[i][:]
    
        return arr

    def check_arr(self,arr):
        for array in arr:
            print(array)
        print()
    
    def extract_position(self):
        position = []
        for i in range(self.n+2):
            for j in range(self.m+2):
                if self.arr[i][j] == '0' or self.arr[i][j] == '6':
                    continue
                else:
                    position.append((self.arr[i][j],(i,j)))
        # print('pos: ', position)
        return position

    def solve_cctv(self):
        position = []
        for cctvnum, (x,y) in self.position:
            if cctvnum == '5':
                self.arrow_fill(self.arr,'left',x,y)
                self.arrow_fill(self.arr,'up',x,y)
                self.arrow_fill(self.arr,'right',x,y)
                self.arrow_fill(self.arr,'down',x,y)
            else:
                position.append((cctvnum,(x,y)))
        self.maxcount = len(position)
        self.position = position
        # print(self.maxcount)
        # self.check_arr(self.arr)
        self.rotate(self.arr, 1)

    def rotate(self, arr, count): # 5번 cctv를 처리하고 온 배열
        # print('count: ', count)
        # print('maxcount: ', self.maxcount)
        # print(count == (self.maxcount + 1))
        if count == (self.maxcount + 1):
            # self.check_arr(arr)
            self.allof.append(self.solve_arr(arr))
            return 
        
        cctvnum, (x,y) = self.position[count - 1]
        # if x == 1:
        #     print('x는 1이다')
        # print('info:' ,cctvnum, x, y)
        ori_arr = copy.deepcopy(arr)
        if cctvnum == '4':
            positive = [
                ['left','up','right'],
                ['up','right','down'],
                ['right','down','left'],
                ['down','left','up']]
            for posit in positive:
                arrs = copy.deepcopy(ori_arr)
                self.arrow_fill(arrs,posit[0],x,y)
                self.arrow_fill(arrs,posit[1],x,y)
                self.arrow_fill(arrs,posit[2],x,y)
                self.rotate(arrs, count+1)
                
        elif cctvnum == '3':
            positive = [
                ['left','up'],
                ['up','right'],
                ['right','down'],
                ['down','left']]
            for posit in positive:
                arrs = copy.deepcopy(ori_arr)
                self.arrow_fill(arrs,posit[0],x,y)
                self.arrow_fill(arrs,posit[1],x,y)
                self.rotate(arrs, count+1)
            
        elif cctvnum == '2':
            positive = [
                ['left','right'],
                ['up','down']]
            for posit in positive:
                arrs = copy.deepcopy(ori_arr)
                self.arrow_fill(arrs,posit[0],x,y)
                self.arrow_fill(arrs,posit[1],x,y)
                self.rotate(arrs, count+1)
                
        else:
            # print('time to 1!')
            positive = ['left','up','right','down']
            for posit in positive:
                arrs = copy.deepcopy(ori_arr)
                self.arrow_fill(arrs,posit,x,y)
                self.rotate(arrs, count+1)
                
        
    def solve_arr(self,arr):
        counts = 0
        for ar in arr:
            counts += ar.count('0')
        return counts
        
        

    # def arrow_find(self, direction, i, j):
    #     if direction == 'left':
    #         x , y = i , j - 1
    #     elif direction == 'up':
    #         x , y = i - 1 , j
    #     elif direction == 'right':
    #         x , y = i , j + 1
    #     else: # down
    #         x , y = i + 1 , j
        
    #     if self.arr[i][j] == '6':
    #         return 0
    #     elif self.arr[i][j] == '0':
    #         return self.arrow_find(direction, x, y) + 1
    #     else:
    #         return self.arrow_find(direction, x, y)
        
    def arrow_fill(self, arr, direction, i, j):
        if direction == 'left':
            x , y = i , j - 1
        elif direction == 'up':
            x , y = i - 1 , j
        elif direction == 'right':
            x , y = i , j + 1
        else: # down
            x , y = i + 1 , j
        
        if arr[i][j] == '6':
            return
        elif arr[i][j] == '0':
            arr[i][j] = '#'
            return self.arrow_fill(arr,direction, x, y)
        else:
            return self.arrow_fill(arr, direction, x, y)

if __name__ == "__main__":
    n, m = list(map(int ,sys.stdin.readline().split()))
    arr = []
    for i in range(n):
        arr.append(sys.stdin.readline().split())
    
    CCTV(n,m,arr)
    