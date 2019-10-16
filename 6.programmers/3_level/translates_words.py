"""단어 변환 (https://programmers.co.kr/learn/courses/30/lessons/43163)
입출력 예
begin	target	words	                        return
hit	    cog	    [hot, dot, dog, lot, log, cog]	4
hit	    cog	    [hot, dot, dog, lot, log]	    0
"""

def get_value(b, t, n):
    # print(b, n)
    return sum([b[i] == t[i] for i in range(n[0])])

def dfs(begin, target, words, cnt, n):
    # print(words)
    # print(begin)
    if begin == target:
        return cnt

    cnt_list = []
    for i, w in enumerate(words):
        if get_value(begin, w, n) == n[0] - 1: # w로 바꿀 수 있음
            # print(begin ,'->', w)
            cnt_list.append(dfs(w, target, words[:i] + words[i+1:] , cnt + 1, n))
    # print(cnt_list)
    cnt_list = list(filter(lambda x: x, cnt_list))
    # print(cnt_list)
    return min(cnt_list) if cnt_list else None
    
def solution(begin, target, words):
    n = len(begin)
    answer = dfs(begin, target, words, 0, [n])
    # print(answer)
    return answer if answer else 0

print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log']))
print(solution('hit','hot',['hot', 'dot', 'dog', 'lot', 'log']))