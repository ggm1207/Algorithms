import sys

def solution(l1,l2):
    i = 0
    for j in range(len(l1)):
        if(l1[j] != l2[j]):
            i = i + 1
    return i

def main():
    A , B = sys.stdin.readline().split(' ')
    
    N = len(B) - len(A)
    varlist = []
    
    for i in range(N+1):
        diff = solution(A, B[i:len(A)+i])
        varlist.append(diff)
    print(min(varlist), end = '')
if __name__ == "__main__":
    main()