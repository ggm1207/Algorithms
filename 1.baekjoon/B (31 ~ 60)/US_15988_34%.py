import sys

depth = [1,1,2]

if __name__ == "__main__":
    t = int(input())
    n_list = []
    for i in range(t):
        n_list.append(int(input()))
    for i in range(3,max(n_list)+1):
        depth.append(sum(depth[-3:]))
    for i in n_list:
        print(depth[i])
