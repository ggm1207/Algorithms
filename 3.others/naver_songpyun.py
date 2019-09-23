import sys
from copy import deepcopy
from collections import defaultdict

def return_depth(re_arr, next_list, prev_list):
  depth = 0
  start = [n for n in re_arr if not prev_list[n] and n in re_arr]
  dd = defaultdict(list)
  while(start):
    nexts = []
    for s in start:
      for n in next_list[s]:
        if n in re_arr:
          nexts.append(n)
      dd[depth].append(s)
    depth += 1
    
    nexts = list(set(nexts))
    start = nexts[:]

  return dd

def return_arr(prev_list, k):
  s = set()
  r = set()
  for p in prev_list[k-1]:
    s.add(p)

  while(s != r):
    r = deepcopy(s)
    for pp in list(s):
      for p in prev_list[pp]:
        s.add(p)
  return list(s)

def solution(cook_times, order, k):
  answer = 0
  cook_len = len(cook_times)
  prev_list = defaultdict(list)
  next_list = defaultdict(list)
  
  for i in range(cook_len):
    prev_list[i]
    next_list[i]
  
  for prev, cur in order:
    prev_list[cur-1].append(prev-1)
    next_list[prev-1].append(cur-1)

  re_arr = return_arr(prev_list, k)
  depth_list = return_depth(re_arr, next_list, prev_list)
  
  for _, v in depth_list.items():
    answer += max([cook_times[val] for val in v])

  answer += cook_times[k-1]

  return [len(re_arr), answer]


print(solution([5,30,15,30,35,20,4],[[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7]], 6))
print(solution([5,30,15,30,35,20,4,50,40],[[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7],[8,9]], 9))
print(solution([5,3,2],[[1,2],[2,3],[1,3]], 3))