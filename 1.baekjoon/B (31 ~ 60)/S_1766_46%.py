import sys
import heapq

MIS = lambda : map(int, sys.stdin.readline().split())

def getIdgZero(idg):
  temp = []
  print(idg.items())
  for k, v in list(idg.items()):
    if not v:
      temp.append(k)
      del idg[k]
  return temp

if __name__ == "__main__":
  N, M = MIS()
  ######## init ########
  nexts = {}
  idg = {}
  for i in range(1,N+1):
    idg[i] = 0
    nexts[i] = []
  ######################

  for _ in range(M):
    easy, hard = MIS()
    idg[hard] += 1
    nexts[easy].append(hard)

  queue = []
  sList = []
  
  for key in idg:
    if not idg[key]:
      heapq.heappush(queue, key)

  for _ in range(1, N+1): # 노드 개수만큼 순회
    # queue += getIdgZero(idg)
    # print(idg.items())
    
    # print(queue)
    # for que in queue: # queue 에 들어간 node 들은 -1 값으로
    #   idg[que] = -1
    # print(idg)
    # queue.sort() # 쉬운 문제부터
    
    node = heapq.heappop(queue)
    for idx in nexts[node]: # node가 가리키는 곳 indegree 내리기
      idg[idx] -= 1
      if not idg[idx]: # 검사를 여기서 해야 시간초과가 안난다....
        heapq.heappush(queue, idx)
        
    sList.append(str(node)) # sList 에 node 쌓기
  # print(sList)
  print(" ".join(sList))