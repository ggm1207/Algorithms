import sys

MIS = lambda : int(sys.stdin.readline())

if __name__ == "__main__":
    Mode = {}
    Num_list = []
    n = MIS()
    for i in range(n):
        a = MIS()
        Num_list.append(a)
        if a in Mode:
            Mode[a] += 1
        else:
            Mode[a] = 1
    
    Num_list.sort()
    length = len(Num_list)

    max_mode = max(Mode.values())
    Mode_list = sorted([a for a,b in Mode.items() if b == max_mode])
    if len(Mode_list) > 1:
        Mode_num = Mode_list[1]
    else:
        Mode_num = Mode_list[0]
    # print(Mode_list)

    # print(Mode_list)
    
    print(int(round(sum(Num_list)/length,0)))
    print(Num_list[(length-1)//2])
    print(Mode_num)
    print(Num_list[-1] - Num_list[0])