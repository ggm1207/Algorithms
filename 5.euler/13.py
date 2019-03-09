

def read():
    f = open('./13T.txt','r')
    return f

if __name__ == "__main__":
    f = read()
    totalnum = 0
    for line in f:
        a = int(line)
        totalnum += a
    print(str(totalnum)[0:10])