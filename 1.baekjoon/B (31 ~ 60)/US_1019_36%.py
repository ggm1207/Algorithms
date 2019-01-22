import math

num_count = [0 for _ in range(10)]

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def countNum(N,pos): # N -> Int
    global num_count
    B = makenine(N,pos)
    B = B // 10
    pos_NUM = (B + 1)*(10**(pos-1))
    num_count = list(map(lambda x: x + pos_NUM, num_count))       
    
    if B == 0:
        num_count[0] -= 1
        for i in num_count:
            print(i, end = ' ')
        return
    countNum(B,pos+1)

def makenine(N,pos):
    while(1):
        if (N % 10) != 9: # if N's last number is nine then stop
            for i in str(N):
                num_count[int(i)] -= 1*(10**(pos-1))
            N = N + 1
        else:
            break
    for i in num_count:
            print(i, end = ' ')
    print('makenine: ', N)
    return N
    


# using recursive
if __name__ == "__main__":
    N = input() # len
    countNum(int(N),1)
    
        