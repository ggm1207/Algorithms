""" 자물쇠와 열쇠(https://programmers.co.kr/learn/courses/30/lessons/60059)
입출력 예
key	                                lock	                            result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true

79%... 어디가 문제냐
93%... 어디가 문제냐 - 응 문제 제대로 안 읽었어 ~
"""

def solution(key, lock):
    key_size = len(key)
    pad_size = key_size - 1
    lock_fill_num = sum([row.count(0) for row in lock])

    def padding(lock ,pad_size):
        lock_size = len(lock)
        width = height = pad_size * 2 + lock_size
        padded_lock = [[1 for _ in range(width)] for _ in range(height)]
        for row in range(pad_size, pad_size + lock_size):
            padded_lock[row][pad_size:pad_size + lock_size] = lock[row - pad_size]
        return padded_lock

    def is_key(key, lock):
        key_1d, lock_1d = sum(key, []), sum(lock, [])
        cnt = 0
        for k, l in zip(key_1d, lock_1d):
            if k == 1 and l == 0:
                cnt += 1
        return cnt

    def key_2d_list(key):
        key_list = [key]
        for _ in range(3):
            rotated = [list(row) for row in zip(*key[::-1])]
            key_list.append(rotated)
            key = rotated
        return key_list

    padded_lock = padding(lock, pad_size)
    key_list = key_2d_list(key)
    pad_width = len(padded_lock)
    for y in range(pad_width - key_size + 1):
        for x in range(pad_width - key_size + 1):
            lock_sub = [padded_lock[sub_y][x:x+key_size] for sub_y in range(y, y + key_size)]
            for key_sub in key_list:
                if is_key(key_sub, lock_sub) == lock_fill_num:
                    return True
    return False

if __name__ == "__main__":
    key = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    lock = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
    lock = [list(map(lambda x:2 if x==1 else x, row)) for row in lock]
    print(lock)
    key_size = len(key)
    pad_size = key_size - 1
    lock_fill_num = sum([row.count(0) for row in lock])
    print(lock_fill_num)

    def padding(lock ,pad_size):
        lock_size = len(lock)
        width = height = pad_size * 2 + lock_size
        padded_lock = [[1 for _ in range(width)] for _ in range(height)]
        for row in range(pad_size, pad_size + lock_size):
            padded_lock[row][pad_size:pad_size + lock_size] = lock[row - pad_size]
        return padded_lock

    def is_key(key, lock):
        key_1d, lock_1d = sum(key, []), sum(lock, [])
        cnt = 0
        for k, l in zip(key_1d, lock_1d):
            if k == 1 and l == 0:
                cnt += 1
        return cnt

    def key_2d_list(key):
        key_list = [key]
        for _ in range(3):
            rotated = [list(row) for row in zip(*key[::-1])]
            key_list.append(rotated)
            key = rotated
        return key_list

    padded_lock = padding(lock, pad_size)
    
    key_list = key_2d_list(key)

    pad_width = len(padded_lock)
    for y in range(pad_width - key_size + 1):
        for x in range(pad_width - key_size + 1):
            lock_sub = [padded_lock[sub_y][x:x+key_size] for sub_y in range(y, y + key_size)]
            for key_sub in key_list:            
                if is_key(key_sub, lock_sub) == lock_fill_num:
                    print('true')
                    break
                    
                    
        
        
        
    