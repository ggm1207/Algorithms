"""2 x n 타일링
입출력 예
n	result
4	5
"""


# 순열문제 같음..
# 아니다 DP다.
# fibonacci 순열인 줄 ㅎㅎ..

# n 이 만약 4라고 주어졌을 때 (1,2,1) ,(2,2) , (1,1,2) 이런식으로 풀면 된다.
# N으로 만들기 문제였나? 그거랑 비슷함 풀이보면 기억날 듯

div_num = 1000000007

def solution(n): # 아 이거 오래걸리네 오래걸리는게 맞긴 했음
    r = [n]
    cnt = 0
    while(r):
        s= []
        for i in r:
            if i-2 == 0:
                cnt = (cnt + 1) % div_num
                s.append(i-1)
            elif i-1 == 0:
                cnt = (cnt + 1) % div_num
            else:
                s.append(i-2)
                s.append(i-1)
        r = s[:]
        # print(r)
    return cnt


def prev_solution(n): # div_num 으로 안 나눠줘서 틀린거였네 ㅎㅎ
    fib = [0, 1]
    div_num = 1000000007
    for i in range(2, n + 2):
        fib[i%2] = (fib[(i-1)%2] + fib[(i-2)%2]) % div_num
    return fib[i%2]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))    
print(solution(5))
print(solution(6))
print(solution(7))
print(prev_solution(1))
print(prev_solution(2))
print(prev_solution(3))
print(prev_solution(4))    
print(prev_solution(5))
print(prev_solution(6))
print(prev_solution(7))
print(prev_solution(60000))