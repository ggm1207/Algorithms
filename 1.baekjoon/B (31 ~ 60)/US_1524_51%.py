import sys

# 문제가 너무 모호하다..

def war_ss():
    _ = input()
    N = list(map(int, sys.stdin.readline().split()))
    M = list(map(int, sys.stdin.readline().split()))
    while(True):
        if (len(M) == 0 or len(N) == 0):
            break
        N_min = min(N) # 세준
        M_min = min(M) # 세빈
        
        if (M_min > N_min):
            N.remove(N_min)
        else:
            M.remove(M_min)
    if (len(N) > 0):
        print('S')
    elif (len(M) > 0):
        print('B')
    else:
        print('C')

        
            


def main():
    T = int(input())
    for i in range(T):
        war_ss()
        input()

if __name__ == "__main__":
    main()