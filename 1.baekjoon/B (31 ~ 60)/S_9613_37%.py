import sys
sys.setrecursionlimit(10000)

def GCD(a,b): 
    if(b==0): 
        return a 
    else: 
        return GCD(b,a%b)

def GCD_TOTAL(args):
    total = 0
    while(1):
        if len(args) > 1:
            a = args[0]
            args.pop(0)
            for arg  in args:
                total += GCD(a,arg)
        else:
            break
    print(total)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        GCD_TOTAL(list(map(int , input().split()))[1:])
        