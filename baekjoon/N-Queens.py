import numpy as np
''' N - Queen 문제'''
def Queens_Num(number):
    global Count
    Count = 0
    init_array(number)
    Check_node(0, number)
    print(Count)

def Check_node(node, number):
    global Count, lists
    if promising(node):
        if node == number:
            Count += 1
        else:
            for i in range(1,number+1):
                lists[node + 1] = i
                Check_node(node+1, number)

def promising(i):
    global lists
    k = 1
    Switch = True
    while k < i and Switch:
        if lists[i] == lists[k] or abs(lists[i] - lists[k]) == abs(i - k):
            Switch = False
        k += 1
    return Switch


def init_array(number):
    global lists
    lists = np.zeros((number+1))

if __name__ == "__main__":
    n = input('n x n 의 n 을 입력해주세요:')
    Queens_Num(int(n))
