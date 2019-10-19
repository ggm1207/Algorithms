"""정수 삼각형 (https://programmers.co.kr/learn/courses/30/lessons/43105)
입출력 예
triangle	                                            result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
"""
# 1시쯤에요 parsing 내일 오전 오후에 끝난다.

def solution(triangle):
    for row in range(0, len(triangle) - 1):
        n_row = [[] for col in range(row + 2)]
        for col in range(row+1):
            cur_value = triangle[row][col]
            n_row[col] += [max(triangle[row+1][col], triangle[row+1][col] + cur_value)]
            n_row[col+1] += [max(triangle[row+1][col+1], triangle[row+1][col+1] + cur_value)]
        n_r = [max(a) for a in n_row]
        triangle[row+1] = n_r
    return max(triangle[row+1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))