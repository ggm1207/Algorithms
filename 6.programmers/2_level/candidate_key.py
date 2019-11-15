"""후보키(https://programmers.co.kr/learn/courses/30/lessons/42890)
relation	                    result
[["100","ryan","music","2"] ,
["200","apeach","math","2"] ,
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]	2
"""
from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = 0
    return answer


if __name__ == "__main__":
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
        ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

    columns = [a for a in zip(relation)]
    print(columns)


    column_num = len(relation[0])
    all_list = [combinations(range(column_num), i) for i in range(1, column_num)]
    print(all_list)
    
    candidate_list = []
    for c_l in all_list: # iterator
        for col_no in c_l:
            print(col_no)
            count = defaultdict(int)
            for tp in zip(relation):
                value = ''.join([tp[0][i] for i in col_no])
                count[value] += 1

            if sum(filter(lambda  x: x > 1,count.values())):
                print(count)
            else:
                candidate_list.append(col_no)
                print('else:', count)
    print(candidate_list)
    print(candidate_list[0][0])
    print(candidate_list[1])