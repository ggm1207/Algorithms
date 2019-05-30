# 부등호

num = [str(i) for i in range(10)]

def fake():
    minlist = num[:k+1]
    maxlist = num[-k-1:][::-1]
    length = k+1
    lists = [maxlist, minlist]
    for li in lists:
        value = ''
        for tup in li:
            value += tup
        if truefalse(tup):
            print("".join(tup))
            break
                
def truefalse(tup):
    flag = True
    for i in range(k):
        if flag:
            if eql[i] == '<':
                flag = tup[i] < tup[i+1]
            else:
                flag = tup[i] > tup[i+1]
    return flag


if __name__ == "__main__":
    k = int(input())
    eql = input().split()
    fake()
    