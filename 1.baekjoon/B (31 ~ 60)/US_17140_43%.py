import copy
import operator

MIS = lambda: map(int,input().split())

# 1 1 
# 2 2
# 3 3
# 가로가 2 세로가 3 -> 가로 확장

def get_width(): # 가로 얻기
    width = []
    for ar in arr:
        count = 0
        for a in ar:
            if a:
            else:
                break
        width.append(count)
        if not ar[0]:
            break
    return max(width)

    
def get_height():
    height = []
    for i in range(100):
        count = 0
        for j in range(100):
            if arr[j][i]:
                count += 1
            else:
                break
        height.append(count)
        if not arr[0][i]:
            break
    return max(height)
            
def expand_arr():
    if get_width() <= get_height():
        expand_width(copy.deepcopy(arr)) # 가로 확장
    else:
        expand_height(copy.deepcopy(arr)) # 세로 확장
    
def expand_width(copyarr):
    for i, ar in enumerate(copyarr):
        dicts = {}
        for j, a in enumerate(ar):
            if a :
                if a in dicts:
                    dicts[a] += 1
                else:
                    dicts[a] = 1
        items = sorted(list(dicts.items()), key = operator.itemgetter(1,0))
        # items 는 정렬 된 값
        length = len(items)
        for a,b in items:
            for j in range(length):
                arr[i][j] = a
                arr[i][j+1] = b
        
# 개수가 많은 것이 뒤로
# 개수가 같을 때는 작은 것이 앞으로
# 수 : 개수

def expand_height(copyarr):
    for i in range(100):
        dicts = {}
        for j in range(100):
            if copyarr[j][i]:
                if copyarr[j][i] in dicts:
                    dicts[copyarr[j][i]] += 1
                else:
                    dicts[copyarr[j][i]] = 1
        items = sorted(list(dicts.items()), key = operator.itemgetter(1,0))
        length = len(items)
        for a,b in items:
            for j in range(length):
                arr[j][i] = a
                arr[j+1][i] = b
                

if __name__ == "__main__":
    r,c,k = MIS()
    arr = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(3):
        arr[i][0] , arr[i][1] , arr[i][2] =  MIS()
    
    count = 0
    for _ in range(1,100+1):
        if arr[r-1][c-1] == k:
            print(count)
            break
        expand_arr()
        count += 1
        