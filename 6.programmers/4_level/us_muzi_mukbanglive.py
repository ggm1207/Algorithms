"""무지의 먹방 라이브(https://programmers.co.kr/learn/courses/30/lessons/42891)
food_times	k	result
[3, 1, 2]	5	1
"""

def solution(food_times, k):
    food_len = len(food_times)

    food_idx = [i+1 for i in range(food_len)]
    food_times, food_idx = map(list, zip(*sorted(zip(food_times, food_idx), reverse=True)))
    
    while(1):
        role_cnt = k // food_len

        if role_cnt > food_times[-1]:
            delete_cnt = food_times.count(food_times[-1])
            food_times = food_times[:-delete_cnt]
            food_idx = food_idx[:-delete_cnt]
            k -= food_len * role_cnt
            food_len -= delete_cnt

            if food_len <= 0:
                return -1
        elif role_cnt:
            k -= food_len * role_cnt
        else:
            break

    food_idx, food_times = map(list, zip(*sorted(zip(food_idx, food_times))))

    if k < len(food_idx):
        return food_idx[k]
    else:
        return -1
    
 
if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5

    # food_times = [i+1 for i in range(20)]
    # k = 5

    food_len = len(food_times)

    food_idx = [i+1 for i in range(food_len)]
    food_times, food_idx = map(list, zip(*sorted(zip(food_times, food_idx), reverse=True)))
    
    while(1):
        role_cnt = k // food_len
        print(food_times)
        if role_cnt >= food_times[-1]:
            delete_cnt = food_times.count(food_times[-1])
            food_times = food_times[:-delete_cnt]
            food_idx = food_idx[:-delete_cnt]
            k -= food_len * role_cnt
            food_len -= delete_cnt

            if food_len <= 0:
                print(-1)
                break
        elif role_cnt:
            k -= food_len * role_cnt
        else:
            break

    print(food_idx, food_times)
    food_idx, food_times = map(list, zip(*sorted(zip(food_idx, food_times))))

    if k < len(food_idx):
        print(food_idx[k])
    else:
        print(-1)
    
