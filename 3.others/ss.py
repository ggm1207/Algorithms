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

def insertion_sorted(lists, num):
    for i, v in enumerate(lists):
        if num < v:
            lists.insert(i, num)
            return lists, i
    lists.append(num)
    return lists, i

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
    
    if check_num == min_v:
      value_list[idx] = help_product[idx][1] * value_list[idx] // help_product[idx][0]
      help_product[idx][0] += 1
      help_product[idx][1] += 1
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
def new_solution(N):
  cnt, num = 1 , 3
  value_list = [6, 6]
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
    print('help_product: ', help_product)
    helper = help_product[idx][:]
    print('helper:', helper)
    del value_list[idx]
    del help_product[idx]
    print(help_product)
    print(help_product[:idx])
    print(help_product[idx:])
    print(value_list)
    # for i in range(1, v_len):
    #   temp = value_list[i]
    #   if temp < min_v:
    #     min_v = temp
    #     idx = i
    
    if check_num == min_v:
      value = helper[1] * min_v // helper[0]
      value_list,idx = insertion_sorted(value_list, value)
      help_product = help_product[:idx] + [[helper[0] + 1, helper[1] + 1]] + help_product[idx:]
      continue

    check_num = min_v
    # print(idx , help_product[idx])
    value = helper[1] * min_v // helper[0]
    value_list,idx = insertion_sorted(value_list, value)
    help_product = help_product[:idx] + [[helper[0] + 1, helper[1] + 1]] + help_product[idx:]
    
    if (helper[1] - helper[0]) == v_len + 1:
      num += 1
      value = product(maketuple(num))
      value_list, idx = insertion_sorted(value_list, value)
      help_product = help_product[:idx] + [[1, num + 1]] + help_product[idx:]

    cnt += 1



n = int(stdin.readline())
print(origin_solution(n))
print(new_solution(n))
