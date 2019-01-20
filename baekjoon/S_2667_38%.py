''' n x n 배열을 입력받아 1로 연결된 값들을 마을로 보고 마을의 수와 집들의 개수 구하는 프로그램.
'''
import sys

def find_one( i , j ):
    if lists[i][j] == 1:
        num = Check_num(i,j)
        return num
    else:
        return None

def Check_num(i,j):
    if 0 <= i <= n-1 and 0 <= j <= n-1:
        if lists[i][j] == 1:
            lists[i][j] = 0
            return Check_num(i - 1, j) + Check_num(i , j - 1) + Check_num(i + 1 , j) + Check_num(i, j + 1) + 1
        else:
            return 0
    return 0

if __name__  == "__main__":
    global lists
    n = input()
    n = int(n)
    lists = []
    num = []
    
    for i in range(int(n)):
        a = list(map(int,list(sys.stdin.readline()[:n])))
        lists.append(a)

    for i in range(n):
        for j in range(n):
            num.append(find_one(i,j))

    num = sorted(list(filter(None.__ne__, num)))
    print(len(num))
    for i in num:
        print(i)
