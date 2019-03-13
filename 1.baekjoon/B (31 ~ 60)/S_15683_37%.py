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
        self.allof = []
        self.solve_cctv()
        # self.check_arr()
        print(min(self.allof))

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
        position = sorted(position)[::-1]
        print('pos: ', position)
        return position

    def solve_cctv(self):
        max_num = 0
        position = []
        for cctvnum, (x,y) in self.position:
            if cctvnum == '5':
                self.arrow_fill(self.arr,'left',x,y)
                self.arrow_fill(self.arr,'up',x,y)
                self.arrow_fill(self.arr,'right',x,y)
                self.arrow_fill(self.arr,'down',x,y)
            else:
                position.append((cctvnum,(x,y)))
        self.position = position # cctv 5번을 제외한 나머지 cctv

        self.maxcount = len(position)
        self.check_arr(self.arr)
        self.rotate(self.arr, 1)
    
    def rotate(self, arr, count):

        if count == self.maxcount:
            self.check_arr(arr)
            self.allof.append(self.solve_arr(arr))
            return 
        
        cctvnum, (x,y) = self.position[count - 1]
        ori_arr = arr
        if cctvnum == '4':
            positive = [
                ['left','up','right'],
                ['up','right','down'],
                ['right','down','left'],
                ['down','left','up']]
            for posit in positive:
                self.arrow_fill(ori_arr,posit[0],x,y)
                self.arrow_fill(ori_arr,posit[1],x,y)
                self.arrow_fill(ori_arr,posit[2],x,y)
                self.rotate(ori_arr, count+1)
                
        elif cctvnum == '3':
            positive = [
                ['left','up'],
                ['up','right'],
                ['right','down'],
                ['down','left']]
            for posit in positive:
                self.arrow_fill(ori_arr,posit[0],x,y)
                self.arrow_fill(ori_arr,posit[1],x,y)
                self.rotate(ori_arr, count+1)
            
        elif cctvnum == '2':
            positive = [
                ['left','right'],
                ['up','down']]
            for posit in positive:
                self.arrow_fill(ori_arr,posit[0],x,y)
                self.arrow_fill(ori_arr,posit[1],x,y)
                self.rotate(ori_arr, count+1)
                
            
        elif cctvnum == '1':
            positive = ['left','up','right','down']
            for posit in positive:
                self.arrow_fill(ori_arr,posit,x,y)
                self.rotate(ori_arr, count+1)
                
        
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
    n, m = list(map(int ,input().split()))
    CCTV(n,m)
    