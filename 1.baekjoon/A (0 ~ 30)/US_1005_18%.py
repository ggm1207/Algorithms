import sys
sys.setrecursionlimit(100000)
MIS = lambda : map(int, sys.stdin.readline().split())

def fake():
    total = 0
    while(1):
        cur = b_num
        nextlist = get_next()
        
        

def get_next():

        
def init_fn():
    b_num , b_rules_num = MIS()
    b_secs = list(MIS())
    b_rule = []
    for _ in range(b_rules_num):
        a,b = MIS()
        b_rule.append((b,a))
    b_win = list(MIS())[0]
    b_rule = sorted(b_rule, reverse = True)
    # r = dict()
    # for s , e in b_rule:
    #     if s in r:
    #         r[s] = r[s] + [e]
    #     else:
    #         r[s] = [e]
    return b_num, b_secs, b_win, b_rule
    
if __name__ == "__main__":
    T = int(input()) # set the loop in Testcase
    for _ in range(T):
        b_num, b_secs, b_win, b_rule = init_fn()
        fake()
    