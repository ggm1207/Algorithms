""" 자물쇠와 열쇠(https://programmers.co.kr/learn/courses/30/lessons/60059)
입출력 예
key	                                lock	                            result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true

79%... 어디가 문제냐
"""
import random

def show_2d(lists):
    for row in lists:
        print(row)
    print() 

def create_4patterns(key):
    key4_1d = [key]
    for _ in range(3):
        rotated = [list(row) for row in zip(*key[::-1])]
        key4_1d.append(rotated)
        key = rotated
    return key4_1d

def padding(need_lock, p_size):
    pad = []
    for i in range(len(need_lock)):
        w_pad = [1 for _ in range(p_size *2 + len(need_lock))]
        w_pad[p_size:p_size + len(need_lock)] = need_lock[i]
        pad.append(w_pad)
    
    h_pad = [[1 for _ in range(p_size * 2 + len(need_lock))] for _ in range(p_size * 2 + len(need_lock))]
    h_pad[p_size:p_size + len(need_lock)] = pad
    return h_pad

def solution(key, lock):
    home_x, home_y = [], []
    lock_size, key_size = len(lock), len(key)

    for y in range(lock_size):
        for x in range(lock_size):
            if lock[y][x] == 0:
                home_x.append(x)
                home_y.append(y)

    if not home_x:
        return True

    max_x, min_x = max(home_x), min(home_x)
    max_y, min_y = max(home_y), min(home_y)

    len_need = max(max_x - min_x + 1, max_y - min_y + 1)

    if len_need > key_size:
        return False

    while(max_x - min_x < key_size - 1):
        if min_x == 0:
            max_x += 1
        else:
            min_x -= 1

    while(max_y - min_y < key_size - 1):
        if min_y == 0:
            max_y += 1
        else:
            min_y -= 1



    need_lock = [row[min_x:max_x + 1] for row in lock[min_y:max_y+1]]

    # show_2d(need_lock)
    pad_lock = padding(need_lock, key_size - 1)
    # show_2d(pad_lock)

    key4 = create_4patterns(key)
    # print(len(pad_lock), key_size)
    for y in range(len(pad_lock) - key_size + 1):
        for x in range(len(pad_lock) - key_size + 1):
            # print(y, x)
            for pattern in key4:
                copy_pad = pad_lock[:]
                for yy, row in enumerate(pattern):
                    copy_pad[y+yy][x:x+len(row)] = list(map(lambda x, y : x or y, copy_pad[y+yy][x:x+len(row)], row))
                if all([all(row) for row in copy_pad]):
                    return True
    return False


if __name__ == "__main__":
    key1 = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
    key2 = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
    lock = [[1, 1, 1,0], [1, 1, 0,1], [1, 0, 1, 1], [1, 0, 1, 1]]
    # lock1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    size = 3
    for i in range(3):
        lock = [[random.randint(0,1) for _ in range(size)] for _ in range(size)]
        # show_2d(lock)
        print(solution(key1, lock))
        
    