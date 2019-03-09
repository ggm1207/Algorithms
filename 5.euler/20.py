def fact(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

if __name__ == "__main__":
    num = fact(100)
    print(num)
    print(list(str(num)))
    lists = list(map(int, list(str(num))))
    a = 0
    print(lists)
    for i in lists:
        a += i
    print(a)