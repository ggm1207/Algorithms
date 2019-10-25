""" 괄호 변환 (https://programmers.co.kr/learn/courses/30/lessons/60058)

입출력 예
p	        result
"(()())()"	"(()())()"
")("	    "()"
"()))((()"	"()(())()"
"""
import sys
sys.setrecursionlimit(100000)

def partition(p):
    count = 0
    for i, c in enumerate(p):
        if c == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            break
    return p[:i+1], p[i+1:]

def is_right(p):
    stack = []
    for i, c in enumerate(p):
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True

def solution(p):
    # print(p)
    if not p:
        return p    
    # 2
    u, v = partition(p)
    # print(u, v)
    # return
    # 3
    if is_right(u):
        return u + solution(v)
    else:
        # 4 - 1
        # 4 - 2
        v = "(" + solution(v) + ")"
        u = u[1:-1]
        return v + "".join(list(map(lambda x:"(" if x == ")" else ")", u)))

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))