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
    # print(namelist)
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
        
def score(li):
    print('도경쓰')
    i=1
    result = 0
    for ch in li:
        #print(ch)
        result2 =0
        for c in ch:
            if c == "\"":
                continue
            result2 += ord(c)-64
        result+=result2*i
        #print(result)
        i+=1
    return result

def dokyung():
    line = open('./22T.txt',"r")
    for i in line:
        list1 = i
        list1=list1.split(",")
    list1=sorted(list1)
    # print(list1)
    a = score(list1)
    print (a)

if __name__ == "__main__":
    main()
    dokyung()
    


# if __name__ == "__main__":
#     main()