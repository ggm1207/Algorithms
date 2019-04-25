from functools import reduce

def combi(n,k):
    if n == k:
        print(1)
        return
    n_klist = list1[n-k+1:n+1]
    k_list = list1[1:k+1]
    nf = reduce(lambda x,y: x*y , n_klist, 1)
    kf = reduce(lambda x,y: x*y , k_list, 1)
    print(nf//kf)


if __name__ == "__main__":
    T = int(input())
    list1 = [i for i in range(31)]
    for i in range(T):
        x, y = map(int, input().split())
        if y > x*2:
            combi(y,x)
        else:
            combi(y,y-x)