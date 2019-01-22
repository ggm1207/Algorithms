import sys
sys.setrecursionlimit(100000)

def check(arr,N,W):
    is_alone = []
    for i in range(N,2*N):
        count = 0
        if arr[i%N] + arr[(i-1)%N] <= W:
            count += 1
        if arr[i%N] + arr[(i+1)%N] <= W:
            count += 1
        if arr[i%N] + arr[(i+(N//2))%N] <= W:
            count += 1
        is_alone.append(count)
    return is_alone

def makegroup(group,N,i):
    if group[i%N] > 0:
        return [group[i%N]] + makegroup(group,N,i-1) + makegroup(group,N,i+1) + makegroup(group,N,i+(N//2))
    else:
        return [0]
    

def choragi(arr,N,W):
    group = []
    is_alone = check(arr,N,W)
    for i in range(N,2*N):
        if is_alone[i%N] > 0:
            group + makegroup(is_alone,N,i)

    print(is_alone)
    #for i in range(N,2*N):
    #    print(arr[i%N])
    
    
    

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N2 , W = list(map(int,sys.stdin.readline().split(' ')))
        a = list(map(int,sys.stdin.readline().split(' ')))
        b = list(map(int,sys.stdin.readline().split(' ')))
    arr = a + b 
    print(arr)
    choragi(arr,N2*2,W)