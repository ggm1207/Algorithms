import sys

def peopleN(n):
    pp = [i for i in range(N)]
    pw = []
    check(n,pp,pw,0)

def check(n,pp,pw,count):
    for a in people[n]:
        pw.append(a)
    if pp == pw:


    for a in pw:

    return

if __name__ == "__main__":
    global N
    N = int(input())
    global people
    people = [[] for _ in range(N)]

    while(1):
        a , b = list(map(int,sys.stdin.readline().split(' ')))
        if a == -1:
            break
        people[a-1].append(b-1)
        people[b-1].append(a-1)
    for i in range(N):
        peopleN(i)