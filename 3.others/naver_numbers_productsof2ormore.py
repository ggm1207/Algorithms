"""느낀점
origin, insertion, bin_search 중에서 백만이 입력으로 주어졌을 때는 insertion이 가장 빨랐다.
value_list의 길이가 생각보다 작아서 bin_search 가 힘을 못 썼을 수도 있다. 백만일때 v_len = 13 이었다.
작은 데이터에 대해서는 origin이 빨랐다. value_list의 길이가 길어져야 bin_search가 빨라질 거 같은데
value_list의 길이는 데이터가 커질 수록 안 늘어날거기 때문에... 좋은 알고리즘은 아니었다.
"""
from sys import stdin
from functools import reduce
from time import time

next_num = lambda tup : tuple(map(lambda x : x + 1, tup))
product = lambda tup : reduce(lambda x, y: x*y, tup)

def maketuple(num):
  return tuple(range(1, num+1))

def timer(func):
    def wrapper(*args, **kargs):
        s = time()
        result = func(*args, **kargs)
        print(func.__name__ , "'s time: ", time() - s)
        return result
    return wrapper

def reverse_insertion_sorted(lists, num):
  for i in range(len(lists))[::-1]:
    if num < lists[i]:
      continue
    lists.insert(i+1, num)
    return lists, i + 1
  lists.insert(i, num)
  return lists, i

def insertion_sorted(lists, num):
  for i, v in enumerate(lists):
      if num < v:
          lists.insert(i, num)
          return lists, i
  lists.append(num)
  return lists, i + 1

def binsearch(lists, num):
  low, high = 0, len(lists) - 1
  while(low < high):
    mid = (low + high) // 2
    if lists[mid] > num:
      high = mid - 1
    elif lists[mid] < num:
      low = mid + 1
    else:
      lists.insert(mid + 1, num)
      return lists, mid + 1
  
  if lists[low] > num:
    lists.insert(low, num)
    return lists , low
  else:
    lists.insert(low + 1, num)
    return lists , low + 1

@timer
def origin_solution(N):
  cnt, num = 1 , 3
  value_list = [product(maketuple(num)), product(maketuple(num))]
  help_product = [[2,4], [1,4]]
  check_num = product(maketuple(2))
  while(1):
    if cnt == N:
      return check_num

    v_len = len(value_list)
    idx = 0

    min_v = value_list[idx]
    for i in range(1, v_len):
      temp = value_list[i]
      if temp < min_v:
        min_v = temp
        idx = i
    
    if check_num == min_v:
      value_list[idx] = help_product[idx][1] * value_list[idx] // help_product[idx][0]
      help_product[idx][0] += 1
      help_product[idx][1] += 1
      if idx == v_len - 1:
        num += 1
        help_product.append([1,num+1])
        value_list.append(product(maketuple(num)))
      continue

    check_num = min_v
    value_list[idx] = help_product[idx][1] * value_list[idx] // help_product[idx][0]
    help_product[idx][0] += 1
    help_product[idx][1] += 1

    if idx == v_len - 1:
      num += 1
      help_product.append([1,num+1])
      value_list.append(product(maketuple(num)))

    cnt += 1

@timer
def new_solution_with_insertion(N):
  cnt, num = 1 , 3
  value_list = [6, 6]
  v_len = 2
  help_product = [(2,4), (1,4)]
  check_num = product(maketuple(2))
  while(1):
    if cnt == N:
      return check_num

    idx = 0

    # min_v = value_list.pop(idx) # value_list 에서 최소값
    # helper = help_product.pop(idx) # 이 방법이 더 느림
    min_v = value_list[idx]
    helper = help_product[idx][:]
    del value_list[idx]
    del help_product[idx]
    
    if check_num == min_v:
      value = helper[1] * min_v // helper[0]
      value_list, idx = insertion_sorted(value_list, value)
      help_product.insert(idx, (helper[0] + 1, helper[1] + 1))
      continue

    check_num = min_v
    value = helper[1] * min_v // helper[0]
    value_list, idx = insertion_sorted(value_list, value)
    help_product.insert(idx, (helper[0] + 1, helper[1] + 1))

    if (helper[1] - helper[0]) == v_len + 1:
      num += 1
      v_len += 1
      value = product(maketuple(num))
      value_list, idx = reverse_insertion_sorted(value_list, value)
      help_product.insert(idx, (1, num + 1))

    cnt += 1

@timer
def new_solution_with_binsearch(N): # value_list 의 길이가 그렇게 길지 않아서 bin_search가 힘을 못 쓰는 듯..
  cnt, num = 1 , 3
  value_list = [6, 6]
  v_len = 2
  help_product = [(2,4), (1,4)]
  check_num = product(maketuple(2))
  while(1):
    if cnt == N:
      return check_num

    idx = 0
    min_v = value_list[idx]
    helper = help_product[idx][:]
    del value_list[idx]
    del help_product[idx]
 
    if check_num == min_v:
      value = helper[1] * min_v // helper[0]
      value_list, idx = binsearch(value_list, value)
      help_product.insert(idx, (helper[0] + 1, helper[1] + 1))
      continue

    check_num = min_v
    value = helper[1] * min_v // helper[0]
    value_list, idx = binsearch(value_list, value)
    help_product.insert(idx, (helper[0] + 1, helper[1] + 1))

    if (helper[1] - helper[0]) == v_len + 1:
      num += 1
      v_len += 1
      value = product(maketuple(num))
      value_list, idx = reverse_insertion_sorted(value_list, value)
      help_product.insert(idx, (1, num + 1))

    cnt += 1

n = int(stdin.readline())

print(new_solution_with_insertion(n))
print(new_solution_with_binsearch(n))
print(origin_solution(n))

