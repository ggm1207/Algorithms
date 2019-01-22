import sys
import math


def check(x, y, r):
    a = math.sqrt(math.pow((x_pos1 - x), 2) + math.pow((y_pos1 - y), 2))
    b = math.sqrt(math.pow((x_pos2 - x), 2) + math.pow((y_pos2 - y), 2))
    c = math.sqrt(math.pow((x_pos2 - x_pos1), 2) +
                  math.pow((y_pos2 - y_pos1), 2))
    if (a < r):
        if(b < r):
            return 0
        else:
            return 1
    else:
        if(b < r):
            return 1
        else:
            return 0


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        startend = list(map(int, sys.stdin.readline().split(' ')))
        num = int(input())
        plant = []
        for i in range(num):
            plant.append(list(map(int, sys.stdin.readline().split(' '))))
        x_pos1 = startend[0]
        y_pos1 = startend[1]
        x_pos2 = startend[2]
        y_pos2 = startend[3]
        a = 0
        for i in range(num):
            a += check(plant[i][0], plant[i][1], plant[i][2])
        print(a)
