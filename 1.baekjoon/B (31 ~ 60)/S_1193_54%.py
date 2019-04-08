if __name__ == "__main__":
    x = int(input())
    i = 1
    sums = 0
    while(1):
        if sums >= x:
            break
        pre_sum = sums
        sums = i*(i+1)/2
        i += 1
    # x = 14 , i = 6 , pre_sum = 10
    if i % 2 == 0:
        directon = 'left'
    else:
        directon = 'right'

    #print('data: ', x , i, pre_sum)
    rightlist = [x for x in range(1,i)]
    leftlist = rightlist[::-1]

    #print(directon)
    count = x - int(pre_sum)
    
    r = rightlist[count - 1]
    l = leftlist[count - 1]
    if directon == 'left':
        print('{}/{}' .format(l,r))
    else:
        print('{}/{}' .format(r,l))


