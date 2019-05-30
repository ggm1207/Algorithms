from sys import stdin
import copy

def fake(N):
    if button:
        prevNum = getNum(N)
    
        length = len(str(prevNum))
        N = int(N)
        val = N - 100
        list1 = [val]
        print(prevNum)

        if prevNum > N:
            list1.append(prevNum - N + length)
        elif prevNum == N:
            list1.append(length)
        else:
            list1.append(N - prevNum + length)
        list1.append(abs(100 - int(N)))
        list1 = list(filter(lambda x : x >= 0, list1))
        print(min(list1))
    else:
        print(abs(100 - int(N)))


# getNum : 번호로 누를 수 있는 최대 가능성
# N : 정답
# 

def getNum(N):
    length = len(N)
    valuelist = ['']
    
    for value in valuelist: # ''
        nextlist = []
        for i in range(1,length):
            number = int(N[0:i+1])
            list1 = [value + btn for btn in button]
            list2 = sorted(list(map(lambda x : abs(number - int(x)), list1)))
            if list2[1]:
                nextlist.append(list2[0])
        
            down = list1[list2.index(min(list2))]
 
        


    if '' in valuelist:
        valuelist.remove('')

    if valuelist[0][0] == '0':
        valuelist[0] = '1' + valuelist[0][1:]

    value = ''
    up = ''
    down = ''
    for btn in button:
        if btn > N[0]:
            up = btn
            break
    
    for btn in button:
        if btn > N[0] or btn == N[0]:
            down = button[button.index(btn)-1]
            break

    if down:
        for i in range(1,length):
            number = int(N[0:i+1])
            list1 = [down + btn for btn in button]
            list2 = list(map(lambda x : abs(number - int(x)), list1))
            print('u ' ,list2)
            down = list1[list2.index(min(list2))]
        valuelist.append(down)
        
    
    if up:
        for i in range(1,length):
            number = int(N[0:i+1])
            list1 = [up + btn for btn in button]
            list2 = list(map(lambda x : abs(number - int(x)), list1))
            print('u ' ,list2)
            up = list1[list2.index(min(list2))]
        valuelist.append(up)
        
            


    # for j in range(2):
    #     if j % 2 == 0:
    #         value =  

    for i in range(0,length):
        number = int(N[0:i+1])
        list1 = [value + btn for btn in button]
        list2 = list(map(lambda x : abs(number - int(x)), list1))
        print('a ' ,list2)
        value = list1[list2.index(min(list2))]

    valuelist.append(value)
    print(valuelist)
    list2 = list(map(lambda x : abs(int(N) - int(x)) + len(x),valuelist))
    print(list2)
    return int(valuelist[list2.index(min(list2))])


if __name__ == "__main__":
    N = stdin.readline().rstrip()
    m = int(stdin.readline())
    if m != 0:
        button = list(stdin.readline().split())
    else:
        button = []
    button = [str(i) for i in range(10) if str(i) not in button]
    # print(button)
    fake(N)