import sys
sys.setrecursionlimit(100000)
MIS = lambda : map(int, sys.stdin.readline().split())

def fake():
    r = set()
    s = set()
    total = b_secs[0]
    while 1 not in r:
        r.add(b_num)
        total += max([b_secs[i-1] for i in list(r)])
        s = r.copy()
        for i in list(s):
            r.update(b_rule[i-1])
        r = r - s
    print(total)
        
def init_fn():
    b_num , b_rules_num = MIS()
    b_secs = MIS()
    b_rule = []
    for _ in range(b_rules_num):
        a,b = MIS()
        b_rule.append((b,a))
    b_win = list(MIS())[0]
    b_rule = sorted(b_rule, reverse = True)
    r = dict()
    for s , e in b_rule:
        if s in r:
            r[s] = r[s] + [e]
        else:
            r[s] = [e]
    return b_num, list(b_secs), b_win, r
    
if __name__ == "__main__":
    T = int(input()) # set the loop in Testcase
    for _ in range(T):
        b_num, b_secs, b_win, b_rule = init_fn()
        fake()
    