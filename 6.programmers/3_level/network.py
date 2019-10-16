"""네트워크 (https://programmers.co.kr/learn/courses/30/lessons/43162)
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""
#* False 인 컴퓨터를 찾는다.
#* 한번 방문한 컴퓨터는 True 값으로 바꾸며 연결되어있는 컴퓨터를 모두 순회한다.
#* 반복
#* 네트워크 개수 return

from collections import defaultdict


def solution(n, computers):
    net_k = defaultdict(bool)
    for i in range(n):
        net_k[i]
    
    cluster_num = 0
    while(not all(net_k.values())): #? all True 일때 끝
        #? False인 컴퓨터를 찾는다.
        for computer, visit in net_k.items():
            if not visit:
                cpt_idx = computer
                break
        net_k[cpt_idx] = True
        # print('find false:', cpt_idx)
        #? networks를 순회한다.
        # next_cpt_idx = list(filter(lambda x : not net_k[x],computers[cpt_idx]))
        next_cpt_idx = [i for i in range(len(computers[cpt_idx])) if not net_k[i] and computers[cpt_idx][i]]
        
        while(next_cpt_idx):
            # print(next_cpt_idx)
            cur_cpt_idx = next_cpt_idx.pop()
            # print('순회: ',cur_cpt_idx)
            net_k[cur_cpt_idx] = True
            next_cpt_idx += [i for i in range(len(computers[cur_cpt_idx])) if not net_k[i] and computers[cur_cpt_idx][i]]
        cluster_num += 1
    return cluster_num

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

