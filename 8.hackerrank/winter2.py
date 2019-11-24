from sys import stdin, stdout
from collections import defaultdict
import math

def beta_var(alpha, beta):
    # return (math.gamma(alpha)*math.gamma(beta))/math.gamma(alpha + beta)
    return alpha*beta / (pow((alpha + beta),2) * (alpha + beta + 1))

if __name__ == "__main__":

    T = int(stdin.readline())
    result = []
    
    beta_init = beta_var(1.0, 15.0)
    for testcase in range(T):

        N = int(stdin.readline())
        Sk = []
        alpha, beta = 1.0, 15.0 # alpha 가 크면 1 beta가 크면 0
        slot_machine = dict() # 슬롯머신의 보상 확률
        visited = defaultdict(bool)
        
        sm_len = 0
        for num in range(N):
            item_id, kind, kind_count = stdin.readline().rstrip('\n').split() # item_id: 콘텐츠 id, imp: 노출, click: 클릭
            item_id, kind_count = int(item_id), int(kind_count)
            flag = False
            if not visited[item_id]:
                flag = True
                visited[item_id] = True
                slot_machine[item_id] = (alpha, beta)
                sm_len += 1

            if kind == 'imp':
                o_alpha, o_beta = slot_machine[item_id]
                slot_machine[item_id] = (o_alpha , o_beta + kind_count)
                add_value = beta_var(o_alpha, o_beta + kind_count)
            else:
                o_alpha, o_beta = slot_machine[item_id]
                slot_machine[item_id] = (o_alpha + kind_count, o_beta - kind_count)
                add_value = beta_var(o_alpha + kind_count, o_beta - kind_count)

            delete_value = 0
            if not flag:
                delete_value = beta_var(o_alpha, o_beta)
            
            if num == 0:
                S = add_value
            else:
                S = result_S_sum - delete_value + add_value

            result_S_sum = S
            S = S / sm_len
            S = math.log(S)
            
            Sk.append(S)
        
        MAX_S = max(Sk)
        MIN_S = min(Sk)
        for i, S in enumerate(Sk):
            if (S - MIN_S) <= (MAX_S - MIN_S) * 0.05:
                stdout.writelines(str(i + 1) + '\n')
                break
