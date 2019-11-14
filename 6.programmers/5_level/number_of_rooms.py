"""방의 개수(https://programmers.co.kr/learn/courses/30/lessons/49190)
arrows	                                                    return
[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	3
오일러의 정리 문제.. 공부했었던건데 까비
v - e + f = 2
"""
from collections import defaultdict
from pprint import pprint

def solution(arrows):
    tails = []
    visited = defaultdict(bool)
    arrow_bfs = defaultdict(set)
    move = {0: (1, 0), 1: (1, 1), 2: (0, 1), 3: (-1, 1), 4: (-1, 0), 5: (-1, -1), 6: (0, -1), 7: (1, -1)} # y x
    
    cur_pos = (0,0)
    visited[cur_pos] = True
    tails.append(cur_pos)

    room_num = 0

    def bfs(next_pos, tail_pos):
        bfs_visited = defaultdict(bool)
        queue = {next_pos}
        n_queue = set()
        while(queue):
            for pos in queue:
                if pos == tail_pos:
                    return True
                if bfs_visited[pos]:
                    continue
                else:
                    bfs_visited[pos] = True
                    n_queue = n_queue.union(arrow_bfs[pos])
            queue = n_queue.copy()
            n_queue = set()
            
    for ar in arrows:
        next_pos =  cur_pos[0] + move[ar][0], cur_pos[1] + move[ar][1]
        arrow_bfs[cur_pos].add(next_pos)
        arrow_bfs[next_pos].add(cur_pos)
        if next_pos in visited: # 방문한 적이 있다.
            if next_pos in tails: # 방문한적 있고 현재 꼬리에 있을 때 
                room_num += 1
            else:
                if bfs(next_pos, tails[0]):
                    room_num += 1
            tails = [next_pos]
        else: # 방문한 적이 없다.
            tails.append(next_pos)

        visited[next_pos] = True
        cur_pos = next_pos
 
    return room_num

# 방문한 적 있는 노드
# # tails 안에 있는지 검사
# # # 있으면 방 생성. tails 짜르기
# # # 없으면 tails 첫 번째 노드와 지금 노드가 이어져 있는지 확인 -> bfs 로 가야되나
# # # # 방에다가 추가
# 방문한 적 없는 노드
# # tails 에 추가

if __name__ == "__main__":
    arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    tails = []
    visited = defaultdict(bool)
    arrow_bfs = defaultdict(set)
    move = {0: (1, 0), 1: (1, 1), 2: (0, 1), 3: (-1, 1), 4: (-1, 0), 5: (-1, -1), 6: (0, -1), 7: (1, -1)} # y x
    
    cur_pos = (0,0)
    visited[cur_pos] = True
    tails.append(cur_pos)

    room_num = 0

    def bfs(next_pos, tail_pos):
        print('bfs:',next_pos, tails)
        bfs_visited = defaultdict(bool)
        queue = {next_pos}
        n_queue = set()
        while(queue):
            print(queue)
            for pos in queue:
                if pos == tail_pos:
                    return True
                if bfs_visited[pos]:
                    continue
                else:
                    bfs_visited[pos] = True
                    n_queue = n_queue.union(arrow_bfs[pos])
            queue = n_queue.copy()
            print(queue)
            n_queue = set()
            
    for ar in arrows:
        next_pos =  cur_pos[0] + move[ar][0], cur_pos[1] + move[ar][1]
        arrow_bfs[cur_pos].add(next_pos)
        arrow_bfs[next_pos].add(cur_pos)
        if next_pos in visited: # 방문한 적이 있다.
            if next_pos in tails: # 방문한적 있고 현재 꼬리에 있을 때 
                room_num += 1
            else:
                if bfs(next_pos, tails[0]):
                    room_num += 1
            tails = [next_pos]
        else: # 방문한 적이 없다.
            tails.append(next_pos)

        visited[next_pos] = True
        cur_pos = next_pos
 
    pprint(arrow_bfs)
    print(room_num)