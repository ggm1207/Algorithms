import sys
sys.setrecursionlimit(100000)

def destiny(b_num, b_secs, b_win, b_rules):
    total_sec = b_secs[b_win-1]
    check = []
    
    while(1):
        arr = []
        c = 0
        for a,b in b_rules:
            if b_win == a:
                arr.append(b)
                check.append(b)
                c += 1
            else:
                continue

        for i in range(c-1):
            del b_rules[0]

        maxs = 0
        for i in arr:
            if b_secs[i-1] > maxs:
                maxs = b_secs[i-1]
                b_win = i
            else:
                continue
        total_sec += maxs

        if not arr:
            print(total_sec)
            break
        
    
    # i 가 다음 b_win
    
        
def init_fn():
    b_num , b_rules_num = list(map(int,sys.stdin.readline().split(' ')))
    b_secs = list(map(int, sys.stdin.readline().split(' ')))
    b_rule = []
    for _ in range(b_rules_num):
        a,b = list(map(int, sys.stdin.readline().split(' ')))
        b_rule.append((b,a))
    b_win = int(sys.stdin.readline())
    b_rule = sorted(b_rule, reverse = True)
    return b_num, b_secs, b_win, b_rule
    
if __name__ == "__main__":
    T = int(input()) # set the loop in Testcase
    for _ in range(T):
        b_num, b_secs, b_win, b_rule = init_fn()
        destiny(b_num, b_secs, b_win, b_rule)