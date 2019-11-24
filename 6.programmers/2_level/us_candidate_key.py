"""후보키(https://programmers.co.kr/learn/courses/30/lessons/42890)
relation	                    result
[["100","ryan","music","2"] ,
["200","apeach","math","2"] ,
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]	2

효율따윈 신경쓰지 않는다.
"""
from itertools import combinations
from collections import defaultdict

def solution(relation):
    columns = [a for a in zip(relation)]

    column_num = len(relation[0])
    all_list = [combinations(range(column_num), i) for i in range(1, column_num)]
    
    candidate_list = []
    for c_l in all_list: # iterator
        for col_no in c_l:
            count = defaultdict(int)
            flag = True
            for tp in zip(relation):
                value = ''.join([tp[0][i] for i in col_no])
                count[value] += 1
                if count[value] > 1:
                    flag = False
                    break
            if flag:
                candidate_list.append(set(col_no))
                
    candidate_list = sorted(candidate_list[::-1], key = len)

    first = candidate_list.pop()
    i = 0
    c_len = len(candidate_list)
    while(1):
        first_len = len(candidate_list)
        prev_len = len(candidate_list)
        i = 0
        while(i < prev_len):
            if first.difference(candidate_list[i]) and not candidate_list[i].difference(first):
                first = candidate_list.pop()
                prev_len -= 1
                i = 0
            i += 1
        cur_len = len(candidate_list)
        if cur_len == first_len:
            break

    return len(candidate_list) + 1


if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
        ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

    column_num = len(relation[0])
    all_list = [combinations(range(column_num), i) for i in range(1, column_num)]
    
    candidate_list = []
    for c_l in all_list: # iterator
        for col_no in c_l:
            count = defaultdict(int)
            flag = True
            for tp in zip(relation):
                value = ''.join([tp[0][i] for i in col_no])
                count[value] += 1
                if count[value] > 1:
                    flag = False
                    break
            if flag:
                candidate_list.append(set(col_no))
                
    
    unique_list = []
    candidate_list = sorted(candidate_list[::-1], key = len)
    print(candidate_list)

    first = candidate_list.pop()
    unique_list.append(first)
    i = 0
    c_len = len(candidate_list)
    while(1):
        first_len = len(candidate_list)
        prev_len = len(candidate_list)
        i = 0
        while(i < prev_len):
            print(i, candidate_list, first)
            if first.difference(candidate_list[i]) and not candidate_list[i].difference(first):
                first = candidate_list.pop()
                prev_len -= 1
                i = 0
            i += 1
        cur_len = len(candidate_list)
        if cur_len == first_len:
            break

    print(candidate_list)