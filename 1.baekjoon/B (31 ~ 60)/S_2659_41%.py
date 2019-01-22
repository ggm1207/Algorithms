import sys
list_clocknum = []

# 만들 수 있는 경우가 소트로 안되네!!


def check_min(num):
    mins = []
    for i in range(4):
        mins.append(num[i % 4]*1000 + num[(i+1) % 4]*100 +
                    num[(i+2) % 4]*10 + num[(i+3) % 4])
    return min(mins)


if __name__ == "__main__":
    nums = list(map(int, sys.stdin.readline().split(' ')))
    num = check_min(nums)
    for i in range(1, nums[0]+1):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):  # 1111 ~ 1119 , 1222 ~ 1229 , 1233 ~ 1239
                    # 여기서 정렬해서 시계수에 추가해야함.
                    list_clocknum.append(check_min([i, j, k, l]))
    list_clocknum = sorted(list(set(list_clocknum)))
    #for i in list_clocknum:
    #    print(i)
    print(list_clocknum.index(num)+1)
    #print(finish - start)
