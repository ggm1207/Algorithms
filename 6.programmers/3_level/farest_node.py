"""가장 먼 노드 (https://programmers.co.kr/learn/courses/30/lessons/49189)
n	vertex	                                                    return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
"""
from collections import defaultdict

def solution(n, edge):
    visited = [False for _ in range(n)]
    visited[0] = True
    arrow = defaultdict(list)
    for f, t in edge:
        arrow[f-1].append(t-1)
        arrow[t-1].append(f-1)
    # print(arrow)

    new_depth_node = arrow[0]
    # print(new_depth_node)
    while(new_depth_node):
        depth_node = list(set(new_depth_node[:]))
        # print(depth_node)
        for idx in depth_node:
            visited[idx] = True

        new_depth_node = []
        for n_idx in depth_node:
            # print(n_idx)
            for a_n_idx in arrow[n_idx]:
                if not visited[a_n_idx]:
                    # print(a_n_idx)
                    new_depth_node.append(a_n_idx)
    # print(depth_node)
    return len(depth_node)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))