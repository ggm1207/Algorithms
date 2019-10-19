from sys import stdin
MIS = lambda : tuple(map(int, stdin.readline().split()))

def isPossible(idx, meeting_list, visited):
    s, e = meeting_list[idx]
    for i , (vs, ve) in enumerate(meeting_list[idx + 1:]):
        if visited[idx + i + 1]:
            if (vs < s <= ve) or (vs <= e < ve):
                return False
    return True


    



if __name__ == "__main__":
    N = int(stdin.readline())
    meeting_list = sorted([MIS() for _ in range(N)], key = lambda x : (x[1] - x[0]))
    visited = [False for _ in range(N)]
    selected = []
    greedy_min = N + 1
    next_first_idx = 0
    print(meeting_list[11:])
    while(True): # 아 왤케 모든 경우 훑는 걸 못하겠냐.......
        idx, tot = next_first_idx, 1
        visited[idx] = True
        idx += 1
        while(True):
            visited[idx] = True
            if idx == N:
                break
            if isPossible(idx, meeting_list, visited) # 방문하지 않았고 추가 가능하면
                visited[idx] = True
                tot += 1
            else:


        next_first_idx += 1
       

    print(tot)