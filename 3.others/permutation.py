# 순열 구해봅시다..
# 조합 구해봅시다..
# 반복문으로
import copy

def permutation():
    result = []
    c = [0]*length
    result.append(copy.copy(value))
    
    i = 0
    while i < length:
        print(i)
        print('v:',value)
        print('c:',c, end = '\n\n')
        if c[i] < i:
            if i % 2 == 0:
                tmp = value[0]
                value[0] = value[i]
                value[i] = tmp
            else:
                tmp = value[c[i]]
                value[c[i]] = value[i]
                value[i] = tmp
            
            result.append(copy.copy(value))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
        
    


# def combination():

if __name__ == "__main__":
    value = list(map(int, input()))
    length = len(value)
    permutation()