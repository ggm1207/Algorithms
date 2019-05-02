import sys
sys.setrecursionlimit(1000000)

def dp(num):
    dp_list = [[num]]
    new_list = []
    while any(dp_list):
        new_list = []
        for dp in dp_list:
            i = min(dp)
            print(i)
            if i >= 3:
                print('dp:', dp)
                new_list.append(dp + [i-1])
                new_list.append(dp + [i-2])
                new_list.append(dp + [i-3])
            elif i >= 2:
                new_list.append(dp + [i-1])
                new_list.append(dp + [i-2])
            elif i >= 1:
                new_list.append(dp + [i-1])
            else:
                new_list.append(dp)
        print(new_list)
        dp_list = new_list
    for a in new_list:
        print(a)
    print(len(new_list))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        dp(n)