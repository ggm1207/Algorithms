import sys
import string
import collections

MIS = lambda : sys.stdin.readline().split()

def ctoi(c):
    c = ord(c)
    if c <= ord('Z'):
        return c - ord('A')
    return c - ord('a') + 26

def itoc(i):
    if i <= ord('Z'):
        return chr(i + ord('A'))
    return chr(i + ord('a'))

def bfs():
    totalFlow = 0
    S, T = 0 , ord('Z') - ord('A')
    # S 가 시작 노드
    # T 가 도착 노드

    while(1):
        prev = [-1 for _ in range(52)]
        # prev : 노드를 방문했는지 검사하는 리스트
        q = collections.deque()
        q.append(S)
        # 시작 노드를 큐에 집어 넣는다.
        while(len(q)):
            cur = q.popleft()
            # cur : 현재 노드
            for nextPos in adj[cur]:
                # 현재 노드와 이어진 노드를 가져온다.
                if prev[nextPos] != -1:
                    # 방문했을시 다음노드로 건너감
                    continue
                if c[cur][nextPos] - f[cur][nextPos] > 0:
                    # 방문을 안했고 유량을 흘려보낼 수 있다면 큐에 노드 추가
                    q.append(nextPos)
                    prev[nextPos] = cur
                    # 경로를 따라가기 위해 만들어 놓는다
                    if nextPos == T:
                    # 다음 노드가 도착노드이면 break -> 경로를 찾음
                        break
        if prev[T] == -1:
        # 도착노드가 -1 이라는 것은 경로를 못 찾았다는 뜻
        # 즉 모든 유량을 다 흘려보냄
            break
        flow = 987654321
        i = T
        while(i != S):
            # 도착노드와 시작노드를 잇는 간선중 흘려보낼 수 있는 최소유량을 찾는다. 
            flow = min(flow, c[prev[i]][i] - f[prev[i]][i])
            i = prev[i]

        i = T
        while(i != S):
            # 도착노드와 시작노드를 잇는 간선에 최소유량을 더한다.
            f[prev[i]][i] += flow
            f[i][prev[i]] -= flow
            i = prev[i]

        totalFlow += flow
    print(totalFlow)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    c = [[0 for _ in range(52)] for _ in range(52)]
    f = [[0 for _ in range(52)] for _ in range(52)]
    adj = [[] for _ in range(52)]
    
    for i in range(N):
        u, v, w = MIS()
        chto, chfrom, w = ctoi(u), ctoi(v) , int(w)
        c[chto][chfrom] += w
        c[chfrom][chto] += w
        adj[chto].append(chfrom)
        adj[chfrom].append(chto)
    bfs()
    
