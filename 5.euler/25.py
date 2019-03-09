def fibo():
    f1 = 1
    f2 = 1
    f3 = 2
    count = 2
    while(True):
        if len(str(f3)) >= 1000:
            print(len(str(f3)))
            print(count)
            break
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        count += 1 

fibo()
