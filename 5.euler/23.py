def find(n):
    b = 0
    for i in range(1, int(n//2 + 1)):
        if (n % i == 0):
            b += i
    return b

def classifi_over():
    overlist = []
    final = []
    for i in range(1,28124):
        if find(i) > i:
            overlist.append(i)
    
    for i in overlist:
        for j in overlist:
            if i + j > 28123:
                continue
            else:
                final.append(i+j)
    final = sorted(list(set(final)))
    print(final)
    return final
    
    # for i in overlist:
    #     if i % 2 == 1:
    #         print(i)

def check(overlist):
    total = 0
    for i in range(1,28124):
        if i not in overlist:
            # print(i)
            # if i == 10:
            #     break
            total += i
    print(total)

if __name__ == "__main__":
    overlist = classifi_over()
    print(len(overlist))
    check(overlist)