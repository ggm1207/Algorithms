import copy
import sys
import operator

sys.setrecursionlimit(1000)

MIS = lambda: map(int,input().split())

width_max_len = 3
height_max_len = 3
# 1 1 
# 2 2
# 3 3
# 가로가 2 세로가 3 -> 가로 확장

# def get_max_width():
#     len_list = []
#     for i in range(height_max_len):
#         count = 0
#         for a in arr[i]:
#             if a:
#                 count += 1
#         len_list.append(count)
#     return max(len_list)

# def get_max_height():
#     len_list = []
#     for i in range(100):
#         count = 0
#         for j in range(100):
#             if arr[j][i]:
#                 count += 1
#         len_list.append(count)
#     return max(len_list)

def expand_arr():
    if height_max_len >= width_max_len:
        expand_width() # R 연산
    else:
        expand_height() # C 연산
    

# R 연산
# 행의 크기가 가장 큰 행을 기준으로 모든 행의 크기가 커지고
# 행으로 정렬 ->
def expand_width():
    # height_max_len = get_max_height()
    global width_max_len, height_max_len
    for i in range(height_max_len):
        dicts = {}
        for j in range(100):
            if arr[i][j] in dicts:
                dicts[arr[i][j]] += 1
            else:
                dicts[arr[i][j]] = 1
        del dicts[0]
        items = sorted(list(dicts.items()), key = operator.itemgetter(1,0))
        #print(items)
        # items 는 정렬 된 값
        # 새로 배열 채워 넣는것. 100까지
        
        fill_len = len(items)*2 # 2
        width_max_len = max((width_max_len,fill_len))

        for l in range(fill_len,width_max_len + 1):
            arr[i][l] = 0

        for k,(a,b) in enumerate(items):
            #print(k , a, b)
            if k > 50:
                break
            arr[i][k*2] = a
            arr[i][k*2+1] = b
        
# C 연산
def expand_height():
    global width_max_len, height_max_len
    # width_max_len = get_max_width()
    for i in range(width_max_len):
        dicts = {}
        for j in range(100):
            if arr[j][i] in dicts:
                dicts[arr[j][i]] += 1
            else:
                dicts[arr[j][i]] = 1
        del dicts[0]
        items = sorted(list(dicts.items()), key = operator.itemgetter(1,0))
        fill_len = len(items)*2
        height_max_len = max((height_max_len, fill_len))
        for l in range(fill_len,height_max_len + 1):
            arr[l][i] = 0
        for k,(a,b) in enumerate(items):
            if k > 50:
                break
            arr[k*2][i] = a
            arr[k*2+1][i] = b
                
if __name__ == "__main__":
    r,c,k = MIS()
    arr = [[0 for _ in range(100)] for _ in range(100)]    

    for i in range(3):
        arr[i][0] , arr[i][1] , arr[i][2] =  MIS()
    
    count = 0
    for _ in range(120):
        # if count == 10:
        #     break
        if arr[r-1][c-1] == k:
            print(count)
            break
        expand_arr()
        # for ar in arr[:10]:
        #     print(ar[:10])
        # print(width_max_len, height_max_len)
        count += 1
        if count == 101:
            print(-1)
            break
        