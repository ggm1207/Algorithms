import sys
tri =[[0 for _ in range(12)] for _ in range(12)]
arr =[[0 for _ in range(12)] for _ in range(12)]
right_triangle1 = [0,0] + [i*i for i in range(2,6)] # [0,0,4,9]
right_triangle2 = [0,0,3,6,10,15,21,28,36,45,55]
change = {'2':3 , '3':5 ,'4':7 , '5':9}
xx = 0

# 1. 들어오는 삼각형은 다 직각 이등변 삼각형
# 2. 아니면 그냥 이상한 도형
# 3. 한 변은 수평선 또는 수직선 -> 이 변을 먼저 찾고
# 4. 외견이 삼각형인지 판별하고
# 5. 그리고 삼각형 내부의 값 확인

def triangle(i,j):
    RRX, RRY, RR_L = RR(i,j,0)
    RDX, RDY, RD_L = RD(i,j,0)
    DDX, DDY, DD_L = DD(i,j,0)
    LDX, LDY, LD_L = LD(i,j,0)
    # 좌표 비교
    pos = []
    pos.append((i,j))

    if RR_L and DD_L: # 1case
        RR_A = RR_L + 1
        DD_A = DD_L + 1
        if RR_A == DD_A:
            if rv(i,j) == right_triangle2[RR_A]:
                pos.append((RRX,RRY))
                pos.append((DDX,DDY))
    if LD_L and RD_L: # 1case
        LD_A = LD_L + 1
        RD_A = RD_L + 1
        if LD_A == RD_A:
            if rv(i,j) == right_triangle1[LD_A]:
                pos.append((LDX,LDY))
                pos.append((RDX,RDY))

    if LD_L and DD_L: # 2case
        LD_A = LD_L + 1
        DD_A = DD_L + 1
        if LD_A == DD_A:
            if rv(i,j) == right_triangle2[LD_A]:
                pos.append((LDX,LDY))
                pos.append((DDX,DDY))
        else: # LD_L < DD
            if change[str(LD_A)] == DD_A:
                if rv(i,j) == right_triangle1[LD_A]:
                    pos.append((LDX,LDY))
                    pos.append((DDX,DDY))
        
    if DD_L and RD_L: # 2case
        RD_A = RD_L + 1
        DD_A = DD_L + 1
        if DD_A == RD_A:
            if rv(i,j) == right_triangle2[RD_A]:
                pos.append((RDX,RDY))
                pos.append((DDX,DDY))
        else: # RD_L < DD
            if change[str(RD_A)] == DD_A:
                if rv(i,j) == right_triangle1[RD_A]:
                    pos.append((RDX,RDY))
                    pos.append((DDX,DDY)) 
    if RD_L and RR_L: # 2case
        RR_A = RR_L + 1
        RD_A = RD_L + 1
        if RD_A == RR_A:
            if rv(i,j) == right_triangle2[RD_A]:
                pos.append((RDX,RDY))
                pos.append((RRX,RRY))
        else: # RD_L < RR_L
            if change[str(RD_A)] == RR_A:
                if rv(i,j) == right_triangle1[RD_A]:
                    pos.append((RDX,RDY))
                    pos.append((RRX,RRY))

    if len(pos) != 3:
        print(xx)
    else:
        pos = sorted(pos)
        for a,b in pos:
            print(a,b)

def rv(i,j):
    if tri[i][j] == 1:
        tri[i][j] = 0
        return rv(i+1,j)+rv(i,j-1) + rv(i,j+1) + 1
    else:
        return 0
def rv_arr(i,j):
    if arr[i][j] == 1:
        arr[i][j] = 0
        return rv_arr(i+1,j) + rv_arr(i,j-1) + rv_arr(i,j+1) + 1
    else:
        return 0
    
def RR(i,j,count):
    if tri[i][j+1] == 1:
        return RR(i,j+1,count+1)
    else:
        return i,j,count    

def RD(i,j,count):
    if tri[i+1][j+1] == 1:
        return RD(i+1,j+1,count+1)
    else:
        return i,j,count
def DD(i,j,count):
    if tri[i+1][j] == 1:
        return DD(i+1,j,count+1)
    else:
        return i,j,count
def LD(i,j,count):
    if tri[i+1][j-1] == 1:
        return LD(i+1,j-1,count+1)
    else:
        return i,j,count

if __name__ == "__main__":
    for i in range(10):
        a = list(map(int,sys.stdin.readline()[:10]))
        tri[i+1][1:11] = a
        arr[i+1][1:11] = a
    count = []    
    for i in range(12):
        for j in range(12):
            if arr[i][j]:
                count.append(rv_arr(i,j))
    
    if len(count) > 1:
        print(xx)
    else:
        for i in range(12):
            for j in range(12):
                if tri[i][j]:
                    triangle(i,j)
                    break
            if tri[i][j]:
                break
        