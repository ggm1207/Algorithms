n = int(input())
sortnum = sorted(map(int,[input() for _ in range(n)]))
for num in sortnum:
    print(num)