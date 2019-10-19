"""N으로 표현 (https://programmers.co.kr/learn/courses/30/lessons/42895)
입출력 예
N	number	return
5	12	    4
2	11	    3
"""

# 나누기 연산에서 나머지는 무시, 즉 // 사용
# 숫자 붙이는 것도 가능하네 55
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# -------------------------------
# New Solution
# 왜 dp인지 이해가 갔다.. 나누기 연산만 없었으면 쉽게 풀었을거 같은데..
# 숫자 4개 사용하는 경우 

def solution(N, number):
    Numbers = [[int(str(N)*(i+1))] for i in range(8)]
    # print(Numbers)
    if number == N:
        return 1

    # print(Numbers)
    for fill_idx in range(1, 8): # 1 ~ 7
        N_len = len(str(Numbers[fill_idx][0]))
        fix_idx , mv_idx = 0, 0
        fix_len, mv_len = len(str(Numbers[fix_idx][0])), len(str(Numbers[mv_idx][0]))
        copy_list = []
        while(1):
            if fix_len + mv_len < N_len: # 해당되지 않을 때
                # print(fix_len, mv_len, end = '%\n')
                mv_idx = mv_idx + 1

            elif fix_len + mv_len == N_len: # 해당 될 때
                # print(fix_len, mv_len, end = '*\n')
                for i in range(len(Numbers[fix_idx])):
                    for j in range(len(Numbers[mv_idx])):
                        value1 = Numbers[mv_idx][j] * Numbers[fix_idx][i]
                        value2 = Numbers[mv_idx][j] + Numbers[fix_idx][i]
                        value3 = Numbers[mv_idx][j] - Numbers[fix_idx][i]
                        value4 = value3
                        if Numbers[fix_idx][i] != 0:
                            value4 = Numbers[mv_idx][j] // Numbers[fix_idx][i]
                        # print(value1, value2, value3, value4)
                        copy_list.extend(list(set((value1, value2, value3, value4))))
                fix_idx = fix_idx + 1
                mv_idx = fix_idx
            else: # 값을 넘었을 때
                # print(fix_len, mv_len, end = '@\n')
                fix_idx = fix_idx + 1
                mv_idx = fix_idx

            fix_len, mv_len = len(str(Numbers[fix_idx][0])), len(str(Numbers[mv_idx][0]))
            
            if fix_len + mv_len > N_len:
                Numbers[fill_idx] = Numbers[fill_idx] + list(set(copy_list))
                if number in Numbers[fill_idx]:
                    return N_len
                break
        # print('*'*30)
        # print(Numbers[fill_idx])

    return -1

def prev_solution(N, number):
    cur_min = 9
    for N_n in range(1,9):
        NG = int(str(N)*N_n)
        N_set = set([NG])
        # print(N_set)
        count = N_n
        while(1):
            if count > 8:
                break
            if number in N_set:
                cur_min = min(cur_min, count)
                break
            N_copy = set()
            for p_v in N_set:
                N_copy.add(p_v + N) # 더하기
                N_copy.add(p_v * N) # 곱하기
                N_copy.add(p_v - N) # 빼기
                N_copy.add(p_v // N) # 나누기
            N_set = N_copy.copy()
            count += 1
    if cur_min > 8:
        return -1
    return cur_min

print(solution(5, 5))
print(solution(5, 55))
print(solution(5, 121))
print(solution(5, 12))
print(solution(5, 2))
print(solution(2, 11))
print(solution(1, 12))
print(solution(1, 32000))
print(solution(2, 32000))
print(solution(3, 32000))
print(solution(4, 32000))
print(solution(5, int(pow(5,6)) + 2))