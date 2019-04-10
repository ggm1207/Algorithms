import sys

def hash_func(data):
    return data % 11

def storage_data(hash_address, data):
    # if (1): if 문 실행
    # if (0): else 문 실행
    # hash_table[hash_address] 
    if hash_table[hash_address]:
        find_store(data)
    else:
        hash_table[hash_address] = data

def get_data(key):
    return hash_table[hash_func(key)]

# 순차검색
def find_store(data):
    print('충돌 발생. 순차검색 실행')
    for i, store in enumerate(hash_table):
        if store:
            print(i ,'번 째 공간에', store ,'데이터가 차 있습니다.')
            continue
        else:
            print(i ,'번 째 공간에', data  ,'데이터 입력.')
            hash_table[i] = data
            break
    print('충돌 해결')
            

hash_table = list([0 for i in range(11)])
print(hash_table)

data_list = [15,558,32,132,102,5,257,257,257]

for i in data_list:
    address = hash_func(i)
    storage_data(address, i)

    sys.stdout.write(str(i))
    sys.stdout.write(" -->\t")
    print(hash_table)
