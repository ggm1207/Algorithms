# 2016-09-15 20:59:57.421 0.351s
# # 
def t2ts(times): # return (start_timestamp, end_time)
    _ , times, proc = times.split()
    ti , es= times.split('.')
    hh, mm, ss = ti.split(':')
    ts = 1000*(int(hh)*3600 + int(mm)*60 + int(ss)) + int(es)
    proc = proc[:-1].split('.')
    if len(proc) == 1:
        proc = int(proc[0]) * 1000 + 1
    else:
        proc = int(proc[0]) * 1000 + int(proc[1]) + 1
    return ts - proc , ts
    
def solution(lines):
    arr = []
    for line in lines:
        s, e = t2ts(line)
        arr.append((s,'s'))
        arr.append((e,'e'))
    arr.sort()
    
    print(arr)
    
    countarr = []
    base, _ = arr[0]
    for i in range(len(arr)):
        base, se = arr[i]
        count = -1
        j = i
        print('base:', base)
        print('-------------')
        while(1):
            if j >= len(arr):
                break
            cts, cse = arr[j]
            print(cts)
            if cts < base + 1000:
                count +=1
                j += 1
            else:
                countarr.append(count)
                break
        print('--------------')
    
    print(countarr)
    print(max(countarr))


arar = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]
solution(arar)  
