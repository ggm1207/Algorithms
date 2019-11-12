""" 외벽 점검 (https://programmers.co.kr/learn/courses/30/lessons/60062)
제한사항
n은 1 이상 200 이하인 자연수입니다.
weak의 길이는 1 이상 15 이하입니다.
서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
weak의 원소는 0 이상 n - 1 이하인 정수입니다.
dist의 길이는 1 이상 8 이하입니다.
dist의 원소는 1 이상 100 이하인 자연수입니다.
친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

입출력 예
n	weak	            dist        	result
12	[1, 5, 6, 10]	    [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]   	1

완전탐색문제...
"""

from itertools import permutations

def get_fnum(dist, weak):
    d_idx, w_idx, add = 0, 0, 1
    f_num = 0
    for w in weak:
        for d in dist:
            

    return f_num


def solution(n, weak, dist):
    weak_list = iter([weak[i:] + weak[:i] for i in range(len(weak))])
    # print(list(weak_list))
    answer = []
    for i in range(len(dist)):
        dist_pt = permutations(dist, i + 1)
        for dist in dist_pt:
            for weak in weak_list:
                answer.append(get_fnum(dist, weak))

    return min(answer) if answer else -1


print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))