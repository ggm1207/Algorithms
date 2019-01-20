import sys

if __name__ == "__main__":
    _ = sys.stdin.readline()
    a = sys.stdin.readline()[:-1]
    tot = 0
    for i in a:
        if i != '0':
            tot += int(i)
    print(tot)
