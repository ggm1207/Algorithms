import sys
MIS = lambda : sys.stdin.readline().split()
num = {}
for i in range(10):
    num[str(i)] = i
print(num)

def nkmin(n,k):
    while(1):
        if k == len(set(str(n))):
            break
        n += 1
    print(n)

# n 은 10^18 보다 작거나 같은 자연수
# k 는 10보다 작거나 같은 자연수
if __name__ == "__main__":
    n, k = MIS()
    nkmin(n,k)