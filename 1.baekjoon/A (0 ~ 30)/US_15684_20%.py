MIS = lambda: map(int,input().split())

import numpy as np

# def main():

# def fill_x(ladder,a,b):
#     ladder[b-1][a-1] = 'l'
#     if b-2 >= 0:
#         ladder[b-2][a-1] = 'x'
#     if b < N-1:
#         ladder[b][a-1] = 'x'


# go and back possible count + 1 and add
# go and back not possible count + 1 and go

def check(line):
    count = 0
    for li_num in range(1,N+1):
        now_li = li_num
        for li_now in range(1,H+1):
            if (now_li, li_row) in line:
                if checking_line(now_li, li_row): # high empty 1 low empty 2
                    now_li = li_row
                else:
                    now_li = li_row + 1 # change line
                
                count += 1
                continue
            if (now_li - 1, li_row) in line:
                if checking_line(now_li, li_row):
                    now_li = li_now + 1
                else:
                    now_li = li_now

                count += 1
                continue
            
def checking_line(line,a):
    if ()



if __name__ == "__main__":
    N, M, H = MIS()
    ladder = []
    line = {}

    # for i in range(N-1):
    #     ladder.append(['0' for _ in range(H)])

    # for _ in range(int(M)):
    #     a, b = MIS()
    #     fill_x(ladder, a, b)

    for _ in range(int(M)):
        a, b = MIS()
        line[(a,b)] = b+1

    print(line)
    for l in line:
        print(l)





# (possible number, line to be modified)
#    
