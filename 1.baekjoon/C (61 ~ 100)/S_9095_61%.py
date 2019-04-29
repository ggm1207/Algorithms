import sys
sys.setrecursionlimit(1000000)



def dp(num):
    dp_list = []
    new_list = []
    dp_list.append(num)
    while any(dp_list):
        new_list = []
        for i in dp_list:
            if i >= 3:
                new_list += [i-1,i-2,i-3]
            elif i >= 2:
                new_list += [i-1,i-2]
            elif i >= 1:
                new_list += [i-1]
            else:
                new_list.append(i)
        dp_list = new_list
    print(len(new_list))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        dp(n)