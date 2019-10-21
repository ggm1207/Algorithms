from sys import stdin
import copy
# 답지 봄
# 가장 빠른 방법은 아니지만 가장 쉽게 풀 수 있는 방법
button = []

def check(num):
    s = str(num)
    lens = len(s)
    for i in range(lens):
        if s[i] not in button: # 여기 줄여야 되는데 귀찮으므로 안 줄임
            return 0
    return lens

if __name__ == "__main__":
    N = int(stdin.readline().rstrip())
    m = int(stdin.readline())
    button = list(stdin.readline().split()) if m != 0 else []
    button = [str(i) for i in range(10) if str(i) not in button]
    # 고장난 버튼들
    ans = abs(100 - N) # ++, -- 로 가는 경우
    for i in range(1000000):
        lens = check(i) # 999999 까지 가면서 최솟값 찾기
        if lens:
            ans = min(abs(N - i) + lens, ans)

    print(ans)