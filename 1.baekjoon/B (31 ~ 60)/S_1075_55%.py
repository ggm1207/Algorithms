import sys

def brute(N,F):
    N = int(N/100) * 100
    for i in range(0,100):
        if((N+i)%F == 0):
            break
    if i < 10:
        print('0'+ str(i))
    else:
        print(i)
    
def main():
    N = int(input())
    F = int(input())
    brute(N,F)

if __name__ == "__main__":
    main()