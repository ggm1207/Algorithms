# 위상 정렬

import sys
sys.setrecursionlimit(100000)
MIS = lambda : map(int, sys.stdin.readline().split())

bTotList = [0 for i in range(1001)]
queue = []

def fake():
    totals = 0
    nextList = [b_win]
    # totals = rec(nextList)
    while(1):
        for i in range(1,b_num + 1): # indegree 가 0 인 노드 queue 에 집어 넣기
            if not indegree[i]:
                queue.append(i)
        
        


    print(totals)

# def rec(nextList):
#     nextList = list(set(nextList))
#     print(nextList)
#     return max([b_secs[np-1] for np in nextList]) + max([rec(b_rule[np]) if np in b_rule else 0 for np in nextList])

def init_fn():
    b_num , b_rules_num = MIS()
    b_secs = [0] + list(MIS())
    b_rule = {}
    indegree = [0 for i in range(b_num+1)]
    for i in range(b_num):
        b_rule[i+1] = []
    for _ in range(b_rules_num):
        a,b = MIS()
        indegree[b] += 1
        b_rule[a].append(b)
    b_win = int(input())
    print(b_num, b_secs, b_win, b_rule)
    return b_num, b_secs, b_win, b_rule, indegree
    
if __name__ == "__main__":
    T = int(input()) # set the loop in Testcase
    for _ in range(T):
        b_num, b_secs, b_win, b_rule, indegree = init_fn()
        fake()
    