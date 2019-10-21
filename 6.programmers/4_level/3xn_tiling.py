"""3 x n 타일링(https://programmers.co.kr/learn/courses/30/lessons/12902)
입출력 예
n	result
4	11

n = 6 // 41
n = 8 // 153
n = 5000 // 658712818

1. 점화식 접근
2. 예외 탐색
3. 예외 해결
"""

def solution(n):
    n = n // 2
    fib_fuck = 3
    for i in range(0, n - 1):
        fib_fuck *= fib_fuck
        fib_fuck += 2
        fib_fuck %= 1000000007
    return fib_fuck

print(solution(2))                                                                                                                                                                                                                 
print(solution(4))                                                                                                                                                                                                              
print(solution(6))
print(solution(8))