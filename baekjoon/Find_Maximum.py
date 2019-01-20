''' N개의 숫자를 입력받고 그 중 가장 큰 값과 위치를 말해준다.'''
def makinglist(n):
    dic_lists = {}
    for i in range(n):
        num = input('숫자 입력:')
        num = int(num)
        dic_lists[i] = num
    lists = sorted(dic_lists.items() , key = lambda x: x[1], reverse = True)
    print('최대값 %d' %lists[0][1])
    print('순서 %d' %(lists[0][0] +1))


if __name__ == "__main__":
    n = input('몇개의 숫자를 입력하실 껀가요:')
    makinglist(int(n))
