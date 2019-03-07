from string import ascii_uppercase

alpha_list = list(ascii_uppercase)
dicts = {}
a = 1
for i in alpha_list:
    dicts[i] = a
    a += 1

# print(dicts)

def read():
    f = open('./22T.txt','r')
    return f

def main():
    f = read()
    total = 0
    for line in f:
        namelist = line.split(',')
    namelist.sort()
    #namelist = sorted(namelist)
    print(namelist)
    for i, name in enumerate(namelist):
        sums = 0
        for alpha in name:
            # print(dicts)    
            if alpha in dicts:
                sums += dicts[alpha]
                # print(sums, muls)
            else:
                continue
        total += sums * (i+1)
    print(total)
        

if __name__ == "__main__":
    main()