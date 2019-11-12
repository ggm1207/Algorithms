""" 블록 이동하기 (https://programmers.co.kr/learn/courses/30/lessons/60063)

제한사항
board의 한 변의 길이는 5 이상 100 이하입니다.
board의 원소는 0 또는 1입니다.
로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

입출력 예
board	                                                                            result
[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	7

교훈.. y , x 로 하자.. 띠바
"""
import copy
import heapq
from collections import defaultdict

def solution(board):
    N = len(board)

    arrow = {0: (0, 1) , 1: (0, -1) , 2: (1, 0), 3: (-1, 0)}
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = defaultdict(bool)
    
    # init
    visited[(0,0,0)] = True
    visited[(0,1,1)] = True
    first_state = (0, (0, 0, 0)), (0, (0, 1, 1))

    queue = []
    heapq.heappush(queue, first_state[0])
    heapq.heappush(queue, first_state[1])

    def can_robot(y,x,ar):
        a_y, a_x = arrow[ar][0] + y, arrow[ar][1] + x
        for v in [y, x, a_y, a_x]:
            if v < 0 or v >= N:
                return False
        return board[y][x] == board[a_y][a_x] == 0
    
    c_ar = lambda ar: ar - 1 if ar % 2 == 1 else ar + 1
    r_ar = lambda ar: [2, 3] if ar < 2 else [0, 1]

    def move_robot(cnt, y,x,ar):
        for mv in move:
            a_y, a_x = mv[0] + y, mv[1] + x
            n_y, n_x = a_y + arrow[ar][0], a_x + arrow[ar][1]
            if can_robot(a_y, a_x, ar) and not visited[(a_y, a_x, ar)]:
                ar_v = arrow[ar]
                visited[(a_y, a_x, ar)] = True
                heapq.heappush(queue, (cnt + 1, (a_y, a_x, ar)))
                if not visited[(n_y, n_x, c_ar(ar))]:
                    visited[(n_y, n_x, c_ar(ar))] = True
                    heapq.heappush(queue, (cnt + 1, (n_y, n_x, c_ar(ar))))

    def rot_robot(cnt, y,x,ar):
        if ar < 2:
            next_ar_list = r_ar(ar) # 2 3
            if not can_robot(y-1, x, ar): # 위로 회전 할 수 없는 경우
                next_ar_list.remove(3)
            if not can_robot(y + 1, x, ar): # 밑으로 회전 할 수 없는 경우
                next_ar_list.remove(2)
            for n_ar in next_ar_list:
                if not visited[(y,x,n_ar)]:
                    ar_v = arrow[n_ar]
                    visited[(y,x,n_ar)] = True
                    heapq.heappush(queue, (cnt + 1, (y, x, n_ar)))
                    if not visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))]:
                        visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))] = True
                        heapq.heappush(queue, (cnt + 1, (y + ar_v[0],x + ar_v[1], c_ar(n_ar))))
        else:
            next_ar_list = r_ar(ar) # 2 3
            if not can_robot(y, x - 1, ar): # 왼쪽으로 회전 할 수 없는 경우
                next_ar_list.remove(1)
            if not can_robot(y, x + 1, ar): # 오른쪽 회전 할 수 없는 경우
                next_ar_list.remove(0)
            for n_ar in next_ar_list:
                if not visited[(y,x,n_ar)]:
                    ar_v = arrow[n_ar]
                    visited[(y,x,n_ar)] = True
                    heapq.heappush(queue, (cnt + 1, (y, x, n_ar)))
                    if not visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))]:
                        visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))] = True
                        heapq.heappush(queue, (cnt + 1, (y + ar_v[0],x + ar_v[1], c_ar(n_ar))))
    while(queue):
        cnt, (y, x, ar) = heapq.heappop(queue)
        if (y,x) == (N-1,N-1) or (y + arrow[ar][0], x + arrow[ar][1]) == (N-1,N-1):
            return cnt
        move_robot(cnt, y, x, ar)
        rot_robot(cnt, y, x, ar)
        show_robot(y, x, ar)

if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    N = len(board)

    arrow = {0: (0, 1) , 1: (0, -1) , 2: (1, 0), 3: (-1, 0)}
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = defaultdict(bool)
    
    # init
    visited[(0,0,0)] = True
    visited[(0,1,1)] = True
    first_state = (0, (0, 0, 0)), (0, (0, 1, 1))

    queue = []
    heapq.heappush(queue, first_state[0])
    heapq.heappush(queue, first_state[1])

    print(queue)

    def can_robot(y,x,ar):
        a_y, a_x = arrow[ar][0] + y, arrow[ar][1] + x
        for v in [y, x, a_y, a_x]:
            if v < 0 or v >= N:
                return False
        return board[y][x] == board[a_y][a_x] == 0
    
    c_ar = lambda ar: ar - 1 if ar % 2 == 1 else ar + 1
    r_ar = lambda ar: [2, 3] if ar < 2 else [0, 1]

    def move_robot(cnt, y,x,ar):
        for mv in move:
            a_y, a_x = mv[0] + y, mv[1] + x
            n_y, n_x = a_y + arrow[ar][0], a_x + arrow[ar][1]
            if can_robot(a_y, a_x, ar) and not visited[(a_y, a_x, ar)]:
                ar_v = arrow[ar]
                visited[(a_y, a_x, ar)] = True
                heapq.heappush(queue, (cnt + 1, (a_y, a_x, ar)))
                if not visited[(n_y, n_x, c_ar(ar))]:
                    visited[(n_y, n_x, c_ar(ar))] = True
                    heapq.heappush(queue, (cnt + 1, (n_y, n_x, c_ar(ar))))

    def rot_robot(cnt, y,x,ar):
        if ar < 2:
            next_ar_list = r_ar(ar) # 2 3
            if not can_robot(y-1, x, ar): # 위로 회전 할 수 없는 경우
                next_ar_list.remove(3)
            if not can_robot(y + 1, x, ar): # 밑으로 회전 할 수 없는 경우
                next_ar_list.remove(2)
            for n_ar in next_ar_list:
                if not visited[(y,x,n_ar)]:
                    ar_v = arrow[n_ar]
                    visited[(y,x,n_ar)] = True
                    heapq.heappush(queue, (cnt + 1, (y, x, n_ar)))
                    if not visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))]:
                        visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))] = True
                        heapq.heappush(queue, (cnt + 1, (y + ar_v[0],x + ar_v[1], c_ar(n_ar))))
        else:
            next_ar_list = r_ar(ar) # 2 3
            if not can_robot(y, x - 1, ar): # 왼쪽으로 회전 할 수 없는 경우
                next_ar_list.remove(1)
            if not can_robot(y, x + 1, ar): # 오른쪽 회전 할 수 없는 경우
                next_ar_list.remove(0)
            for n_ar in next_ar_list:
                if not visited[(y,x,n_ar)]:
                    ar_v = arrow[n_ar]
                    visited[(y,x,n_ar)] = True
                    heapq.heappush(queue, (cnt + 1, (y, x, n_ar)))
                    if not visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))]:
                        visited[(y + ar_v[0],x + ar_v[1], c_ar(n_ar))] = True
                        heapq.heappush(queue, (cnt + 1, (y + ar_v[0],x + ar_v[1], c_ar(n_ar))))

    def show_robot(y, x, ar):
        a_y, a_x = y + arrow[ar][0], x + arrow[ar][1]
        copy_board = copy.deepcopy(board)
        copy_board[y][x] = 2
        copy_board[a_y][a_x] = 2
        for row in copy_board:
            print(row)
        print()

    while(queue):
        cnt, (y, x, ar) = heapq.heappop(queue)
        if (y,x) == (N-1,N-1) or (y + arrow[ar][0], x + arrow[ar][1]) == (N-1,N-1):
            print(cnt)
            break
        move_robot(cnt, y, x, ar)
        rot_robot(cnt, y, x, ar)
        print(cnt)
        show_robot(y, x, ar)

        # print(y, x, ar)
        # print(visited)

    for row in board:
        print(row)