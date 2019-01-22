import sys

def count(a):
    fib0 = 1
    fib1 = 1
    if a== 0:
        return fib0
    elif a == 1:
        return fib1
    else:
        for i in range(a-1):
            result = fib0 + fib1
            fib0 = fib1
            fib1 = result
        return result
    
def fibo(a):
    fib0 = 0
    fib1 = 1
    if a== 0:
        return fib0
    elif a == 1:
        return fib1
    else:
        for i in range(a-1):
            result = fib0 + fib1
            fib0 = fib1
            fib1 = result
        return result 
        

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a = int(sys.stdin.readline())
        print((count(a) - fibo(a)),fibo(a))