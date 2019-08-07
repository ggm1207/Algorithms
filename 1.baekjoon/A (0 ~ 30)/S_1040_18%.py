import sys

MIS = lambda : sys.stdin.readline().split()

nums = {}
for i in range(10):
    nums[str(i)] = i

def getSetLen(N : str):
    # if type(N) == int:
    #     N = str(N)
    return len(set(N))

def fake(N : str ,K : str):
    N_len = len(N)
    K = int(K)
    if getSetLen(N) == K:
        return N
    for idx, digit in enumerate(N[::-1]): # IN N
        for up in range(nums[digit] + 1, 10):
            N = N[:N_len - (idx+1)] + str(up)
            leftlen = K - getSetLen(N) # 추가되어야 하는 종류의 갯수
            rightlen = idx # 추가되어야 하는 길이
            # print(leftlen, rightlen)
            if leftlen < 0 or leftlen > rightlen: 
                continue
            used = sorted(list(set(N)))
            unUsed = nums.keys() - set(N)
            unUsed = sorted(list(unUsed))
            if leftlen == 0:
                return N + used[0]*rightlen
            return N + '0'*(rightlen - leftlen) + "".join(unUsed[:leftlen])
    # AFTER N -> N + 1
    N_len = max(K , N_len + 1)
    return "1"+"0"*(N_len - K + 1)+"23456789"[:K-2]

# n 은 10^18 보다 작거나 같은 자연수
# k 는 10보다 작거나 같은 자연수
if __name__ == "__main__":
    N, K = MIS()
    print(fake(N,K))