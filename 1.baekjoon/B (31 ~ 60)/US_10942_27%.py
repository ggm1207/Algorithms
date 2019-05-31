from sys import stdin

MIS = lambda : stdin.readline().split()

if __name__ == "__main__":
    N = int(stdin.readline())
    value = "".join(list(MIS()))
    M = int(stdin.readline())
    Mlist = [list(map(int,MIS())) for _ in range(M)]
    for S, E in Mlist:
        print(int(value[S-1:E] == value[S-1:E][::-1]))
    

