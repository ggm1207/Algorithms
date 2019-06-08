''' n의 약수들의 합과 n 이 같은지를 판별'''
import numpy as np
from string import ascii_uppercase

def Find_divisors(num):
    lists = []
    lists_1 = []
    number = num
    prime_list = [2,3,5,7,11,13,17,19]
    while True:
        for i in prime_list:
            if number%i == 0:
                #print(i , end = '  ') ; print(number)
                number = int(number/i)
                lists.append(i)
            else:
                lists_1.append(i)
        lists_1 = list(set(sorted(lists_1)))
        if lists_1 == prime_list:
            break
    if number != num:
        lists.append(number)

    for i in range(1, int(number//2 +1)):
        if number % i == 0:
            lists.append(i)
    lists = sorted(lists)
    lists2 = {}
    print(lists)
    for i in lists:
        lists2[i] = 0
    for i in lists:
        lists2[i] +=1
    print(lists2)


if __name__ == "__main__":
    while True:
        number = int(input())
        if number == -1:
            break
        Find_divisors(number)
