"""셔틀버스 (https://programmers.co.kr/learn/courses/30/lessons/17678)
n	t	m	timetable	                        answer
1	1	5	[08:00, 08:01, 08:02, 08:03]	    09:00
2	10	2	[09:10, 09:09, 08:00]	            09:09
2	1	2	[09:00, 09:00, 09:00, 09:00]	    08:59
1	1	5	[00:01, 00:01, 00:01, 00:01, 00:01]	00:00
1	1	1	[23:59]	                            09:00
"""

def time2hm(time):
    h, m = divmod(time, 60)
    return "{:0>2}:{:0>2}".format(h, m)

def hm2time(hm):
    h, m = hm.split(':')
    h = int(h) * 60
    return h + int(m)

def solution(n, t, m, timetable):
    bus_stime = hm2time("09:00")
    bus_arrive_dicts = {bus_stime + i*t : [] for i in range(n)}
    timetable = sorted(list(map(hm2time, timetable)))

    for time in timetable:
        for bus_time in bus_arrive_dicts.keys():
            if len(bus_arrive_dicts[bus_time]) == m:
                continue
            if time <= bus_time:
                bus_arrive_dicts[bus_time].append(time)
                break
    bus_timelist = sorted(bus_arrive_dicts.keys(), reverse=True)

    if n == 1:
        buses = bus_arrive_dicts[bus_timelist[0]]
        if len(buses) < m:
            return time2hm(bus_timelist[0])

        if buses[0] == buses[-1]:
            return time2hm(buses[0] -1)
        else:
            return time2hm(buses[-1] -1)
    
    for b_idx in range(len(bus_timelist)-1):
        late_bus = bus_arrive_dicts[bus_timelist[b_idx]]
        fast_bus = bus_arrive_dicts[bus_timelist[b_idx + 1]]

        if len(late_bus) < m: # late_bus 인원 수가 꽉 안 찼을 때
            return time2hm(bus_timelist[b_idx])
        
        if late_bus[0] == late_bus[-1]: # late_bus에서 해결이 안 될때
            if len(fast_bus) < m: # fast_bus 인원 수가 꽉 안 찼을 때
                return time2hm(bus_timelist[b_idx + 1])
                
            # fast_bus 도 인원 수 꽉 찬 경우 나열
            if fast_bus[0] == late_bus[0]: # 다음 경우까지 봐야할때
                continue
            elif fast_bus[-1] != late_bus[0]: # last_bus 처음 보다 빨리 오면 탐 
                return time2hm(late_bus[0] - 1)
                
            elif fast_bus[-1] == late_bus[0]: # fast_bus 마지막보다 빨리 오면 탐
                return time2hm(fast_bus[-1] -1)
            
        else: # late_bus 에서 해결 될 때
            return time2hm(late_bus[-1]) -1
            
    return time2hm(fast_bus[0] -1)
    
            

if __name__ == "__main__":
    n , t, m = 2, 10, 2
    timetable = ["09:10", "09:09", "08:00"]

    # n , t, m = 10, 60, 45
    # timetable = ["23:59" for i in range(16)]

    # n , t, m = 2, 1, 2
    # timetable = ["00:01", "00:01", "00:02", "00:02","00:02"]

    bus_stime = hm2time("09:00")
    bus_arrive_dicts = {bus_stime + i*t : [] for i in range(n)}
    timetable = sorted(list(map(hm2time, timetable)))
    print(bus_stime)
    print(bus_arrive_dicts)

    for time in timetable:
        for bus_time in bus_arrive_dicts.keys():
            if len(bus_arrive_dicts[bus_time]) == m:
                continue
            if time <= bus_time:
                bus_arrive_dicts[bus_time].append(time)
                break
    print(bus_arrive_dicts)
    bus_timelist = sorted(bus_arrive_dicts.keys(), reverse=True)
    print(bus_timelist)
    for b_idx in range(len(bus_timelist)-1):
        late_bus = bus_arrive_dicts[bus_timelist[b_idx]]
        fast_bus = bus_arrive_dicts[bus_timelist[b_idx + 1]]

        if len(late_bus) < m: # late_bus 인원 수가 꽉 안 찼을 때
            print(time2hm(bus_timelist[b_idx]))
            break
        
        if late_bus[0] == late_bus[-1]: # late_bus에서 해결이 안 될때
            if len(fast_bus) < m: # fast_bus 인원 수가 꽉 안 찼을 때
                print(time2hm(bus_timelist[b_idx + 1]))
                break
l
            # fast_bus 도 인원 수 꽉 찬 경우 나열
            if fast_bus[0] == late_bus[0]: # 다음 경우까지 봐야할때
                continue
            elif fast_bus[-1] != late_bus[0]: # last_bus 처음 보다 빨리 오면 탐 
                print(time2hm(late_bus[0] - 1))
                break
            elif fast_bus[-1] == late_bus[0]: # fast_bus 마지막보다 빨리 오면 탐
                print(time2hm(fast_bus[-1] -1))
            
        else: # late_bus 에서 해결 될 때
            print(time2hm(late_bus[-1] -1))
            break

    print(time2hm(fast_bus[0] -1))
    
    
    

            

    


