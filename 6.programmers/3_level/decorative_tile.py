"""타일 장식물 (https://programmers.co.kr/learn/courses/30/lessons/43104)
입출력 예
N	return
5	26
6	42
"""

def solution(N):
    fib = [1, 1, 2, 3]
    if N == 1:
        return 4
    elif N == 2:
        return 6
    elif N == 3:
        return 10
    elif N == 4:
        return 16

    for i in range(4,N):
        fib[i % 4] = fib[(i-1) % 4] + fib[(i-2) % 4]
    return fib[i%4] * 3 + (fib[(i-1)%4] + fib[(i-2)%4]) * 2 + fib[(i-3)%4]

print(solution(5))
print(solution(6))