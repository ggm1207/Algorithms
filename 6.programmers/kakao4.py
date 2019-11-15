from collections import defaultdict
import random

# union-find 문제라는 개념을 알고 나서 풀었다...
# 나도 이런식으로 접근할려 했는데 왜 안되었을까..
# 문제 다시 풀기는 귀찮으니.. 밑에 설명..
# dict 에서 합쳐지면 아래있는 값을 배열에서 변경하면 됨. 그럼 시간 오래 안 걸림
def solution(k, room_number):
    answer = []
    next_room_number = dict()
    for rn in room_number:
        next_room_number[rn] = rn
    
    for i, rn in enumerate(room_number):

        if rn == next_room_number[rn]:
            answer.append(rn)
            next_room_number[rn] += 1
            continue

        n_rn = next_room_number[rn]

        while(n_rn in next_room_number):
            n_rn = next_room_number[n_rn]

        answer.append(n_rn)
        next_room_number[n_rn] = n_rn + 1
        next_room_number[rn] = next_room_number[n_rn]
        
    return answer

if __name__ == "__main__":
    k = 10
    room_number = [1,3,4,1,3,1,2,5]
    answer = []
    next_room_number = dict()

    for rn in room_number:
        next_room_number[rn] = rn
    
    for i, rn in enumerate(room_number):
        prev_rn = rn
        while(rn in next_room_number):
            if rn == next_room_number[rn]:
                answer.append(rn)
                next_room_number[rn] += 1
                flag = True
                break
            prev_rn = rn
            rn = next_room_number[rn]
        if flag:
            flag = False
            continue
            
        answer.append(rn)
        next_room_number[prev_rn] += 1

    print(answer)
    print(next_room_number)        
    