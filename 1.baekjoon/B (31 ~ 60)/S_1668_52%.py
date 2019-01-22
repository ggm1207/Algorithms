import sys

def left_or_right(lists, MAXNUM):
    left_var = lists[0]
    i = 1
    for a in range(1,60):
        if(left_var == MAXNUM):
            print(i)
            break
        if(lists[a] > left_var):
            left_var = lists[a]
            i = i + 1
            continue
        
def main():
    N = int(sys.stdin.readline())
    tropys = []
    for _ in range(N):
        tropys.append(int(sys.stdin.readline()))
    max_heigh = max(tropys)
    left_or_right(tropys, max_heigh)
    left_or_right(tropys[::-1], max_heigh)
    

if __name__ == "__main__":
    main()