"""추석 트래픽 (https://programmers.co.kr/learn/courses/30/lessons/17676)
입력: [ # 최대 2000개
2016-09-15 01:00:04.001 2.0s,
2016-09-15 01:00:07.000 2s
]

출력: 1

초당 최대 처리량: 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초간 처리하는 요청의 최대 개수를 의미한다.

1. 문제 접근
2. 세분화
"""
from datetime import datetime
from collections import defaultdict
import heapq

def lines_to_timestamp(line):
    _, S, T = line.split()
    h, m, st = S.split(':')
    s, t = st.split('.')
    end = int(h) * 3600 + int(m) * 60 + int(s) + float('.' + t)
    start = end - float(T[:-1]) + 0.001
    return round(start, 4), round(end, 4) 

def make_dict_and_lists(lines):
    get_kind_dicts = defaultdict(list)
    end_time_list = []
    start_time_list = []
    for line in lines:
        start, end = lines_to_timestamp(line)
        get_kind_dicts[start].append(True)
        get_kind_dicts[end].append(False)
        end_time_list.append(end)
        start_time_list.append(start)

    return get_kind_dicts, sorted(end_time_list, reverse= True), sorted(start_time_list, reverse=True)

def solution(lines):
    get_kind_dicts, end_time_list, start_time_list = make_dict_and_lists(lines)
    print(end_time_list + start_time_list)
    max_num = 0
    cur_count = 0
    e_idx, s_idx = 0, 0
    while(s_idx != len(start_time_list) and e_idx != len(end_time_list)):
        if s_idx == len(start_time_list):
            s_idx = len(start_time_list) - 1
        
        if e_idx == len(end_time_list):
            e_idx = len(end_time_list) - 1
           
        cur_stime = start_time_list[s_idx]
        cur_etime = end_time_list[e_idx]
        print(cur_etime - 1, cur_stime)
        if cur_etime - 1 < cur_stime:
            s_idx += 1
            cur_count += 1
            max_num = max(cur_count, max_num)
        elif cur_etime - 0.999 == cur_stime:
            s_idx += 1
            e_idx += 1
            max_num = max(cur_count + 1, max_num)
        else:
            e_idx += 1
            cur_count -= 1
    return max_num
        

lines1 = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

lines2 = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(lines1))
print(solution(lines2))