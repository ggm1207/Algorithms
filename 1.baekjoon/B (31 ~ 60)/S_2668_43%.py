import sys

direction = [0]
cycles = []
seq = []
# 1. 1 로 돌아오는 노드가 있고 1이 cycle을 형성하지 않으면 출발
# 2. 첫 시작노드롤 잘 돌아오는 경우 1 -> 2 -> 3 -> 4 -> 1
# 3. 중간에 cycle이 있는 경우 1 -> 2 -> 3 -> 4 -> 2

def count(n_node): #(시작 노드, 현재 노드, 순서)
    seq.append(n_node)
    global cycles
    if direction[n_node] in seq: # 다음 노드가 순서에 있을 경우    
        a = seq.index(direction[n_node])
        cycles = cycles + seq[a:]
        return
    else:
        count(direction[n_node])


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a = int(sys.stdin.readline())
        direction.append(a)
    
    for i in range(n):
        seq = []
        if i+1 in direction and i+1 not in cycles:
            count(i+1)
    cycles = sorted(list(set(cycles)))
    print(len(cycles))
    for i in cycles:
        print(i)
