"""3 x n 타일링(https://programmers.co.kr/learn/courses/30/lessons/12902)
입출력 예
n	result
4	11

n = 6 // 41
n = 8 // 153
n = 12 // 2131
n = 5000 // 658712818

1. 점화식 접근
2. 예외 탐색
3. 예외 해결
-- 답지 보고 이해가 안되서 열심히 이해하고 내가 다시 설명 -- 참고: https://velog.io/@songjy6565/3-x-n-%ED%83%80%EC%9D%BC%EB%A7%81
참고 블로그 읽고와야 이해 가능
1. 점화식은 f(n + 2) = 3*f(n) + ( f(n) - f(n-1) )
2. 예외는 f(n) - f(n-1) 이 된다.
3. 3 * f(n) 은 f(n) 까지 나온 경우의 수에 타일 2칸을 더 추가하므로 2칸에서 나올 수 있는 경우의 수 3을 곱해준다.
4. 이제 예외를 처리해야 하는데 예외는 추가한 타일 2칸과 그 전의 타일 2칸을 조작하여서 예외를 만들 수 있는 경우의 수를 보이면 된다.
5. 즉, 추가한 타일 2칸 옆에 올 수 있는 모든 타일의 경우의 수는 f(n) 이다.
6. 그리고 추가한 타일 2칸 옆에 올 수 있는 = 가로 2개가 위치한 경우의 수가 f(n - 2)이다.
7. 그러면 조작 가능한 경우의 수가 f(n) - f(n-2) 가 된다. 이것이 예외가 됨.
8. 설명 똥같이 했네
"""

def solution(num):
    n, p = 11, 3
    if num % 2:
        return 0
    elif num == 2:
        return 3
    elif num == 4:
        return 11 
    else:
        for _ in range(num//2 - 2):
            temp = (n * 4 - p) % 1000000007
            p = n
            n = temp
    return temp

print(solution(2))                                                                                                                                                                                                                 
print(solution(4))                                                                                                                                                                                                              
print(solution(6))
print(solution(8))