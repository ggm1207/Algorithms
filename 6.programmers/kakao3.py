
# 우선 불량 사용자에 매핑되는 것을 구한 후 결과 제출
# 안되면
# 불량 사용자에 동일하게 매핑되는 경우 해결

from collections import defaultdict
from copy import copy

def is_mapping(b_id, u_id):
    s_counts = b_id.count('*')
    e_counts = sum(list(map(lambda x, y : x == y, b_id, u_id)))
    if s_counts + e_counts == len(b_id):
        return True
    return False

def solution(user_id, banned_id):
    all_list = []
    def dfs(depth, banned_id, user_id, lists):
        if depth == len(banned_id):
            all_list.append(tuple(lists))
            return
        b_id = banned_id[depth]
        for u_id in user_id:
            c_lists = copy(lists)
            if len(b_id) == len(u_id):
                if is_mapping(b_id, u_id):
                    c_lists.append(u_id)
                    user_ids = copy(user_id)
                    user_ids.remove(u_id)
                    dfs(depth+1, banned_id, user_ids, c_lists)
    dfs(0, banned_id, user_id, [])
    real_list = []
    for cc in all_list:
        count = 1
        for name in cc:
            count *= prime_dict[name]
        real_list.append(count)

    return len(set(real_list))

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    
    prime = [2, 3, 5, 7, 11, 13, 17, 19]

    prime_dict = {k:v for k, v in zip(user_id, prime)}
    print(prime_dict)
    

    
    
    # dicts = {k :[] for k in banned_id}
    
                    

    
    # for b_id in dicts.keys():

        
    
