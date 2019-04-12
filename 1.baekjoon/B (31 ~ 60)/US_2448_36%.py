import math
def stars(n, count): # arr 접근 가능
    if count > N:
        return
    if arr[count-1][n] == " ":
        arr[count-1][n] = "*"
    else:
        arr[count-1][n] = " "

    if count % 3 == 1:
        only_star(n - 1, count + 1)
        only_star(n + 1, count + 1) # 2번째

        only_star(n + 2,count + 2)
        only_star(n + 1,count + 2)
        only_star(n    ,count + 2)
        only_star(n - 1,count + 2)
        only_star(n - 2,count + 2) # 3번째
    stars(n + 3, count + 3)
    stars(n - 3, count + 3)

# 재귀 세번 느낌상

def only_star(n, count):
    if arr[count-1][n] == " ":
        arr[count-1][n] = "*"
    else:
        arr[count-1][n] = " "
    return

if __name__ == "__main__":
    N = int(input())
    k = int(math.log2(N / 3))
    print(k)
    

    arr =  [[' ' for _ in range(2*N + 1)] for _ in range(N)]

    # stars(N,1)
    
    # for i in arr:
    #     print(''.join(i))
