import sys
if __name__ == "__main__":
    inp = []
    for i in range(100):
        a = sys.stdin.readline()
        inp.append(a)
    for s in inp:
        if not s:
            break
        print(s, end='')
