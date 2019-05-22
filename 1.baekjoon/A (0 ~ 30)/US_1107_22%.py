from sys import stdin

def fake(N):
    prevNum = getNum(N)
    
    # print(prevNum)
    length = len(N)
    N = int(N)
    val = N - 100
    list1 = [val]

    if prevNum > N:
        list1.append(prevNum - N + length)
    elif prevNum == N:
        list1.append(length)
    else:
        list1.append(N - prevNum + length)

def getNum(N):
    length = len(N)
    num = 0
    check = 'first'
    value = ''
    for i in range(length):
        number = int(N[0:i+1])
        list1 = [value + btn for btn in button]
        list2 = list(map(lambda x : abs(number - int(x)), list1))
        value = list1[list2.index(min(list2))]
    return int(value)

if __name__ == "__main__":
    N = stdin.readline().rstrip()
    m = int(stdin.readline())
    button = list(stdin.readline().split())
    button = [str(i) for i in range(10) if str(i) not in button]    
    fake(N)