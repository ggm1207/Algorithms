import sys
sys.setrecursionlimit(100000)
# 1 ~ 10000
pelins = []
pelins_length = []

def calcu():
    b = 1
    while(1):
        if b >= 10000:
            break
        pelins_length.append(b)
        b = 2*b + 1

def find_nested(k_pelin):
    k, pelin = k_pelin
    p_len = len(pelin)
    
    Bench_mark = []
    a_val = []

    if p_len in pelins_length: # 길이가 짝수면 끝
        print(-1)
        return
    else:
        if is_pelin(pelin):
            for i in range(p_len):
                
                if i%2 == 0: # a_val
                    a_val.append(pelin[i])
                else:
                    Bench_mark.append(pelin[i])

            Bench = list(set(Bench_mark))
            checka = list(set(a_val))
            a_promising = []
            if len(checka) == 2:
                checka.pop('?')
                a_promising.append(checka.pop())
            elif len(checka) == 1:
                a_promising = [i for i in range(1,10)]
                for bm in Bench:
                    a_promising.pop(bm)
            else:
                print(-1)
                return
            Bn = Bench.count('?')


                
        
        for i in range(p_len):
            if pelin[i] == '?':
                pelin[i] = str(k-1)
            print(pelin)
    aaa = []
    # 기준점 물음표 시발
    for i in range(1,10): # 기준점이 1~9 까지 다 있는지 확인
        if i in BM:
            aaa.append(1)
    
    if sum(aaa) == 9: # 확인
        print(-1)
        return
            
    
def is_pelin(pelin):
    p_len = len(pelin)   
    if p_len == 1:
        return True
    else:
        pelin_for = pelin[:p_len//2]
        pelin_back = pelin[(p_len//2)+1:]

    if pelin == pelin[::-1]:
        return is_pelin(pelin_for) and is_pelin(pelin_back)
    else:
        return False

def continue_two(pelin): # 마지막에 체크용
    p_len = len(pelin)
    var = True
    for i in range(p_len-1):
        var = var and (pelin[i] != pelin[i+1])
    return var
            
    




if __name__ == "__main__":
    while(1):
        k = int(input())
        if k == 0:
            break
        pelin = list(sys.stdin.readline())[:-1]
        pelins.append((k,pelin))
    
    calcu()
    for i in pelins:
        find_nested(i)
    