# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

MIS = lambda : tuple(map(int, stdin.readline().split()))

def dist(p1, p2):
    return (p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])
    #return pow(p1[0] - p2[0],2) + pow(p1[1] - p2[1],2)

def _closet_pair(xy_pos, N):
    if N == 2:
        return dist(xy_pos[0], xy_pos[1])
    if N == 3:
        return min(dist(xy_pos[0], xy_pos[1]),dist(xy_pos[1], xy_pos[2]),dist(xy_pos[2], xy_pos[0]))
    half = int(N/2)
    d = min(_closet_pair(xy_pos[:half], half), _closet_pair(xy_pos[half:], N - half))
    lf, rf, i, l_list, r_list = True, True, 0, [], []
    line = (xy_pos[half-1][0] + xy_pos[half][0])/2
    while((lf or rf) and (half-1-i >= 0 and half-1+i < N)):
        # print(half-1-i, half+i)
        # print(lf or rf)
        # sleep(0.1)
        if lf:
            if xy_pos[half-1-i][0] > line - d:
                l_list.append(xy_pos[half-1-i]) # insert 느리대
            else:
                lf = False
        if rf:
            if xy_pos[half+i][0] < line + d:
                r_list.append(xy_pos[half+i])
            else:
                rf = False
        i += 1
    l_list = sorted(l_list[::-1], key = lambda x: x[1])
    r_list = sorted(r_list, key = lambda x: x[1])
    m_list, i, j = [], 0, 0
    while(i < len(l_list) and j < len(r_list)):
        if l_list[i] < r_list[j]:
            m_list.append(l_list[i])
            i += 1
        else:
            m_list.append(r_list[j])
            j += 1

    if i == len(l_list):
        for v in r_list[j:]:
            m_list.append(v)
    else:
        for v in l_list[i:]:
            m_list.append(v)
    
    for i, (cur_x, cur_y) in enumerate(m_list):
        for x, y in m_list[i+1:i+6]:
            d = min(dist((cur_x,cur_y),(x,y)), d)
    
    return d
            
def _main():
    N = int(stdin.readline().rstrip('\n'))
    xy_pos = sorted([MIS() for _ in range(N)])
    d = _closet_pair(xy_pos, N)
    print(d)

if __name__ == "__main__":
	_main()