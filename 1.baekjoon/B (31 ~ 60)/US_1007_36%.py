import sys
MIS = lambda : tuple(map(int,sys.stdin.readline().split()))

def main():
    N_pos =  int(sys.stdin.readline())
    M_position = [MIS() for _ in range(N_pos)]
    print(M_position)

# sqrt(a^2 + b^2)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        main()