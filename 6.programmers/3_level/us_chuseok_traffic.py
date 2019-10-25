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
from dateutil.parser import parse
import datetime
from collections import defaultdict
import heapq

def lines_to_timestamp(line):
    Str_time = line.split(' ')
    duration = float(Str_time[2][:-1])
    end_time = parse(" ".join(Str_time[:2]))
    start = end_time - datetime.timedelta(seconds = (duration - 0.001))
    return start, end_time

def get_sorted_timelist(lines):
    time_list = []
    for line in lines:
        start, end = lines_to_timestamp(line)
        time_list.append([start,end])
    return sorted(time_list)

def solution(lines):
    timelist = get_sorted_timelist(lines)
    max_count = 0
    for time in timelist:
        start, end = time
        count = 0
        for log in timelist:
            if 


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