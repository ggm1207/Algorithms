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

# [1, 2, 4, 5] 3
# 0 3 -> 1
# 1 3 -> 2
# 1 2 -> 1

def binsearch(lists, num):
  low, high = 0, len(lists) - 1
  # print(low, high)
  while(low < high):
    mid = (low + high) // 2 # mid is index
    if lists[mid] > num:
      high = mid - 1
    elif lists[mid] < num:
      low = mid + 1
    else:
      # print(num, 'happen')
      lists.insert(mid + 1, num)
      return lists, mid + 1
  
  if lists[low] > num:
    # print('low')
    lists.insert(low, num)
    return lists , low
  else:
    # print('low + 1')
    lists.insert(low + 1, num)
    return lists , low + 1

@timer
def origin_solution(N):
  cnt, num = 1 , 3
  value_list = [product(maketuple(num)), product(maketuple(num))]
  help_product = [[2,4], [1,4]]
  check_num = product(maketuple(2))
  # min_v = product(value_list[0])
  while(1):
    # print(value_list)
    if cnt == N:
      return check_num

    v_len = len(value_list)
    idx = 0

    min_v = value_list[idx] # value_list 에서 최소값
    for i in range(1, v_len):
      temp = value_list[i]
      if temp < min_v:
        min_v = temp
        idx = i
    # print(value_list, idx, sep = '\n')
    
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
    # print(idx , help_product[idx])
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
  help_product = [(2,4), (1,4)]
  check_num = product(maketuple(2))
  # min_v = product(value_list[0])
  while(1):
    # print(value_list)
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

    v_len = len(value_list)
    if (helper[1] - helper[0]) == v_len + 1:
      num += 1
      value = product(maketuple(num))
      value_list, idx = reverse_insertion_sorted(value_list, value)
      help_product.insert(idx, (1, num + 1))

    cnt += 1

@timer
def new_solution_with_binsearch(N): # value_list 의 길이가 그렇게 길지 않아서 bin_search가 힘을 못 쓰는 듯..
  cnt, num = 1 , 3
  value_list = [6, 6]
  help_product = [(2,4), (1,4)]
  check_num = product(maketuple(2))
  while(1):
    # print(value_list)
    # if value_list == [720, 720, 756, 840]:
    #   print(helper)
    #   break
    if cnt == N:
      return check_num

    idx = 0
    
    min_v = value_list[idx]
    helper = help_product[idx][:]
    del value_list[idx]
    del help_product[idx]
    
    # print(helper)
    # min_v = value_list[idx]
    # helper = help_product[idx][:]
    # del value_list[idx]
    # del help_product[idx]
    
    if check_num == min_v:
      value = helper[1] * min_v // helper[0]
      value_list, idx = binsearch(value_list, value)
      help_product.insert(idx, (helper[0] + 1, helper[1] + 1))
      continue

    check_num = min_v
    value = helper[1] * min_v // helper[0]
    value_list, idx = binsearch(value_list, value)
    help_product.insert(idx, (helper[0] + 1, helper[1] + 1))

    v_len = len(value_list)
    if (helper[1] - helper[0]) == v_len + 1:
      num += 1
      value = product(maketuple(num))
      value_list, idx = reverse_insertion_sorted(value_list, value)
      help_product.insert(idx, (1, num + 1))

    cnt += 1

n = int(stdin.readline())

print(new_solution_with_insertion(n))
print(new_solution_with_binsearch(n))
print(origin_solution(n))

