from itertools import combinations

MIS = lambda : list(map(int,input().split()))

def laboratory(positions):
    for x,y in positions:
        arr[x][y] = '0'

    for x,y in positions:
        count(x+1,y,(1,0),1)
        count(x-1,y,(-1,0),1)
        count(x,y+1,(0,1),1)
        count(x,y-1,(0,-1),1)
        maxnum = [max(ar) for ar in arr]

def count(x,y,arrow, count):
    if not (0 <= x <= N) or not (0 <= y <= N):
        return
    if type(arr[x][y]) == num
        if arr[x][y] > count:
            arr[x][y] = count
        else:
            return
    
    arr[x][y] = count
    
    x += arrow[0]
    y += arrow[1]
    count(x,y,arrow,count+1)
    
if __name__ == "__main__":
    N , M = MIS()
    arr = [MIS() for _ in range(N)]
    pos = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                arr[i][j] = '*'
                pos.append((i,j))
            elif arr[i][j] == 1:
                arr[i][j] = '-'
            else:
                arr[i][j] = '1'

    for ar in arr:
        print(ar)ㄴ
    # 1 이 빈 칸, * 이 비 활성 바이러스, - 이 벽
    comb = list(combinations(pos, M))
    print(comb)

    for positions in comb:
        laboratory(positions)

                

    
    