from sys import stdin, stdout

def kangaroo():
    x1, v1, x2, v2 = map(int, stdin.readline().rstrip('\n').split(' '))
    slow_k, fast_k = ([x1, v1], [x2, v2]) if v1 < v2 else ([x2, v2], [x1, v1])

    if fast_k[1] == slow_k[1]:
        if fast_k[0] != slow_k[0]:
            stdout.writelines('NO')
        else:
            stdout.writelines('YES')
        return 

    while(fast_k[0] <= slow_k[0]):
        if fast_k[0] == slow_k[0]:
            stdout.writelines('YES')
            return
        fast_k[0] += fast_k[1]
        slow_k[0] += slow_k[1]

    stdout.writelines('NO') 

if __name__ == "__main__":
    kangaroo()