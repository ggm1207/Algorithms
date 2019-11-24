def solution(w,h):
    linear = lambda y : - (w / h) * (y - h)
    count = 0

    for i in range(1, h + 1):
        if linear(i) == int(linear(i)):
            continue
        count += 2

    return w * h - count

if __name__ == "__main__":
    # w, h = 8, 12
    w, h = 1, 4
    linear = lambda y : - (w / h) * (y - h)
    count = 0

    for i in range(1, h + 1):
        if linear(i) == int(linear(i)):
            continue
        count += 2

    print(w * h - count)