from tqdm import tqdm
from time import time
MAX_NUM = 1000001

def check(n : int):
  n_list = str(n)
  for j in range(len(n_list)):
    if (n_list[j] in (n_list[0:j] + n_list[j+1:len(n_list)])):
      return 0
  return 1
    
def mains(n):
  count = [check(i) for i in range(1,n)]
  print(n - sum(count) - 1)


a = [0 for i in range(MAX_NUM)]

def check_dp():
  for i in range(1, MAX_NUM):
    a[i] = check(i) + a[i-1]

N = int(input())

b = time()
mains(N)
c = time()
print(c - b)

b = time()
check_dp()
c = time()
print(c-b)

print(a[N - 1])
