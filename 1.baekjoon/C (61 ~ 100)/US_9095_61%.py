
list1 = [[1 for _ in range(11)] for _ in range(11)]

for i in range(2,11):
    for j in range(1,i):
        list1[i][j] = list1[i-j][j-1] + list1[i-j][j]


if __name__ == "__main__":
    for l1 in list1:
        print(l1)
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum(list1[n-1][1:n]))

    