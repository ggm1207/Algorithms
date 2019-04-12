from functools import reduce

if __name__ == "__main__":
    input()
    arr = sorted(list(map(int,input().split())))
    total = 0 
    for i in range(len(arr)):
        total += reduce(lambda x, y : x + y, arr[:i+1])
    print(total)