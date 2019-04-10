def mains():
    Bnum = input().split('-')
    print(Bnum)
    Bnum = ''.join(Bnum)
    print(Bnum)
    # print(Bnum)
    total = 0
    istrue = True
    a = 1
    for i in Bnum:
        total += a * int(i)
        if istrue:
            a = 3
            istrue = False
        else:
            a = 1
            istrue = True
            
    if total%10 == 0:
        print(0)
    else:
        print(10 - total%10)
        
if __name__ == "__main__":
    mains()