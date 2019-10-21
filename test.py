from collections import defaultdict

grid = [[3,4,5],[2,3,4],[1,2,3]]
K = 1
grid1 = [[2,1,1,0,1],[1,2,0,3,0],[0,1,5,1,2],[0,0,1,3,1],[1,2,0,1,1]]
K1 = 2

grid_dict = defaultdict(int)

def sum_K(y,x,K, grid):
  tot = 0
  for y_v in range(y, y + K):
    for x_v in range(x, x + K):
      # print(y_v, x_v)
      tot += grid[y_v][x_v]
  return tot

def solution(grid, K):
  # grid N X N ,  2 <= N <= 500
  # 1 <= K <= N / 2
  N = len(grid)
  
  for h in range(N - K + 1):
    for w in range(N - K + 1):
      grid_dict[(h,w)] = sum_K(h,w,K,grid)

  kv = list(grid_dict.items())
  kv = sorted(kv, key = lambda x : x[1])[::-1]
  k_lt = K - 1 # k_lt 가 0 이면 자기자신 1이면 주위 1칸씩
  print(kv) # kv 의 좌표만 사용
  
  best = 0
  while(1): # grid
    pos, value = kv[best]
    rest_list = kv[:best] + kv[best + 1:]
    for p, v in rest_list:
      y, x = p
      if 

    break

  return 0

print(solution(grid, K))
print(solution(grid1, K1))