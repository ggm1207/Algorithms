import numpy as np

# def main():



if __name__ == "__main__":
    # 첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 
    # 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. 
    N, M, H = list(map(int, input().split()))
    width = []
    for i in range(M):
        width.append(tuple(map(int, input().split())))
    # 가로선의 정보는 두 정수 a과 b로 나타낸다. 
    # (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 
    # a번 점선 위치에서 연결했다는 의미이다.
    
    # for w in width:
    #     print(w)

    