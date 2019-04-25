import sys

def count(a):
    fib0, fib1 = 1,1
    if a <= 1:
        return 1
    else:
        for i in range(a-1):
            fib1 = fib0 + fib1
            fib0 =  fib1 - fib0
        return fib1
    
def fibo(a):
    fib0, fib1 = 0 , 1
    if a <= 1 :
        return a
    else:
        for i in range(a-1):
            fib1 = fib0 + fib1
            fib0 =  fib1 - fib0
        return fib1
        

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = int(sys.stdin.readline())
        b = fibo(a)
        print((count(a) - b),b)