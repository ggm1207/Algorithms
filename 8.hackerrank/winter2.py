from sys import stdin, stdout
from collections import defaultdict
import math

def beta_var(alpha, beta):
    return alpha*beta / (pow((alpha + beta),2) * (alpha + beta + 1))

if __name__ == "__main__":

    T = int(stdin.readline())       # Test Case
    result = []                     # unused
    
    beta_init = beta_var(1.0, 15.0) # unused
    for testcase in range(T):

        N = int(stdin.readline())       # 100 ~ 100000
        Sk = []                         # k 번째 피드백까지 등장한 슬롯머신들의 분산들의 평균에 자연로그 스케일을 적용한 값들의 리스트
        alpha, beta = 1.0, 15.0         # alpha, beta 초기 값
        slot_machine = dict()           # slot_machine[item_id] = (alpha, beta)
        visited = defaultdict(bool)     # slot_machine 방문했는지 안했는지 검사
        
        sm_len = 0
        for num in range(N):
            item_id, kind, kind_count = stdin.readline().rstrip('\n').split() # 피드백
            item_id, kind_count = int(item_id), int(kind_count)
            flag = False
            if not visited[item_id]:    #! 처음 등장한 slot machine 일 경우
                flag = True
                visited[item_id] = True
                slot_machine[item_id] = (alpha, beta)
                sm_len += 1

            if kind == 'imp':   #! 노출
                o_alpha, o_beta = slot_machine[item_id]
                slot_machine[item_id] = (o_alpha , o_beta + kind_count)             #*  보상확률 갱신
                add_value = beta_var(o_alpha, o_beta + kind_count)                  #   더할 값
            else:               #! 클릭
                o_alpha, o_beta = slot_machine[item_id]
                slot_machine[item_id] = (o_alpha + kind_count, o_beta - kind_count) #*  보상확률 갱신
                add_value = beta_var(o_alpha + kind_count, o_beta - kind_count)     #   더할 값

            delete_value = 0                                                        #?  뺄 값 (처음 등장한 slot_machine)
            if not flag:
                delete_value = beta_var(o_alpha, o_beta)                            #?  뺄 값 (기존에 있는 경우)
            # 처음 등장한 slot matchine 일 경우 delete_value는 0의 값을 가진다

            if num == 0: # 처음엔 무조건 더하는 경우만 존재한다.
                S = add_value
            else:
                S = result_S_sum - delete_value + add_value

            result_S_sum = S # k 번째 피드백까지 등장한 슬롯머신들의 분산의 합
            S = S / sm_len # 평균
            S = math.log(S) # 자연로그 스케일을 적용한 값
            
            Sk.append(S)
        
        MAX_S = max(Sk) # S1 ~ SN 의 최댓값
        MIN_S = min(Sk) # S1 ~ SN 의 최솟값
        for i, S in enumerate(Sk):
            if (S - MIN_S) <= (MAX_S - MIN_S) * 0.05:
                stdout.writelines(str(i + 1) + '\n') # 위 조건 만족할 시 break
                break
