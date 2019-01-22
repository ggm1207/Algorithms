import sys
# 평면에 네 개의 직사각형의 넓이 구하는 문제, 중요한건 겹친다..
# 1. 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
# 2. 포함하고 있나 확인 -> 포함되어 있는 것들은 삭제.
# 3. 겹쳐져 있나 안 겹쳐져 있나를 확인. -> 안 겹쳐져 있는 것들은 따로 계산.
# 4. 겹쳐져 있는
# 위 처럼 복잡하게 생각하다 쉽게 풀었다..

xy_plat = [[0 for _ in range(100)] for _ in range(100)]
pos = []


def make_rec(a):
    for i in range(pos[a][0], pos[a][2]):
        for j in range(pos[a][1], pos[a][3]):
            xy_plat[j][i] = 1


if __name__ == "__main__":
    for i in range(4):
        pos.append(list(map(int, sys.stdin.readline().split(' '))))
    max_x = max([pos[0][2], pos[1][2], pos[2][2], pos[3][2]])
    max_y = max([pos[0][3], pos[1][3], pos[2][3], pos[3][3]])
    for i in range(4):
        make_rec(i)
    count = 0
    for i in range(max_x):
        for j in range(max_y):
            if xy_plat[j][i]:
                count += 1
    print(count)
