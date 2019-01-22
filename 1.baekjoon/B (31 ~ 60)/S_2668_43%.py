import sys
sys.setrecursionlimit(100000)
# DFS 문제
direction = []
cycles = []

def promising(i):
    if i in direction: # i 가 순환될 가능성이 있다는 뜻
        if i not in cycles: # 아직 i가 순환된 경우가 없다는 뜻
            cycles + cycle(i,direction[i], [i]) # 그럼 순환 체크해보자.


def cycle(start, node, seq):
    if direction[node] in cycles:       # 부분 시퀀스
        b = seq.index(direction[node])
        return seq[b:]
    if start == direction[node]:                   # 전체 시퀀스
        return seq
    else:
        cycle(start, direction[node] , seq + [node])

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        direction.append(int(sys.stdin.readline()))

    for i in range(N):
        promising(i)

