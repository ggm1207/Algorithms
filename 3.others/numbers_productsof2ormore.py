from sys import stdin
from functools import reduce

next_num = lambda tup : tuple(map(lambda x : x + 1, tup))
product = lambda tup : reduce(lambda x, y: x*y, tup)

def maketuple(num):
  return tuple(range(1, num+1))

def solution(N):
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

print(solution(int(stdin.readline())))