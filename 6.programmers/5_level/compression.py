from string import ascii_uppercase

def solution(msg):
    dicts = {}
    for i, aph in enumerate(ascii_uppercase):
        dicts[aph] = i+1
    check = i+2
    # print(dicts)
    # print(i, check)
    answer = []
    i = 0
    for _ in range(0,len(msg)+1):
        j = i+1
        while(1): # 현재 입력에서 매칭 안될때까지 하나씩 늘리기
            if j > len(msg):
                break
            if msg[i:j] in dicts:
                j += 1
                continue
            else:
                dicts[msg[i:j]] = check
                check += 1
                break
        if j > len(msg):
            answer.append(dicts[msg[i:]])
            break
        answer.append(dicts[msg[i:j-1]])
        i += len(msg[i:j-1])
    return answer