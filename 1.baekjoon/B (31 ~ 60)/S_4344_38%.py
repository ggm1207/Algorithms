import sys
MIS = lambda : map(int,sys.stdin.readline().split())

def fake(cnt, pp):
    avg = sum(pp)/cnt
    up = sum([1 for i in pp if i > avg])
    num = up/cnt*100
    msg = '%.3f' %num + '%'
    print(msg)
    
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        list1 = list(MIS())
        fake(list1[0],list1[1:])