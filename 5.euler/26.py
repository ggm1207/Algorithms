def cyclenumber(n):
    # 몫 : quot
    # 나머지 : rest
    # 나눠야 하는 숫자 : num
    # 나누는 숫자 : att
    num = 1
    att = n
    div_list = []
    count = 0
    while(True):
        if (num , att) in div_list:
            print(count)
            break
        
        while(True):
            if num >= att:
                break
            else:
                num*10
                count += 1

        div_list.append((num,att)) 
        quot , num = divmod(num, att)
        
        if num == 0: # 순환마디가 없는 경우
            break

# def main():
        
    
if __name__ == "__main__":
    for i in range(1,10):
        cyclenumber(i)


