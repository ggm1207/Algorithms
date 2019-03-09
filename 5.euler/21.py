dicts = {}

def make_dict():
    for i in range(1, 10001):
        b = find(i)
        dicts[i] = b
    check(dicts)

def check(dicts):
    total = 0
    origin = list(dicts.items())
    revers = []
    for a, b in origin:
        revers.append((b,a))
    for (a,b) in origin:
        if (a,b) in revers:
            if a == b:
                continue
            total += a
    print(total)

def find(n):
    b = 0
    for i in range(1, int(n//2 + 1)):
        if (n % i == 0):
            b += i
    return b


if __name__ == "__main__":
    make_dict()