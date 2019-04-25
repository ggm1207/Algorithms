from sys import stdin
import heapq

h = []
def fake():
    while(1):
        if len(h):
            pr , (n,num) = heapq.heappop(h)
            #print(pr , n , num)
            if n == 1:
                print(num)
                break
            if not n%3:
                heapq.heappush(h, (n//3 + (num+1)*(num+1)*(num+1)*(num+1)*(num+1), (n//3,num+1)))
            if not n%2:
                heapq.heappush(h, (n//2 + (num+1)*(num+1)*(num+1)*(num+1)*(num+1), (n//2,num+1)))
            heapq.heappush(h, (n - 1+ (num+1)*(num+1)*(num+1)*(num+1)*(num+1), (n-1,num+1)))

if __name__ == "__main__":
    n = next(stdin)
    heapq.heappush(h, (1, ((int(n),0))))
    fake()
# 이건 집합이네...
# N=int(input())
# s=set()
# r=set()
# result=0
# s.add(N)
# while 1 not in s:
# 	result+=1
# 	k=s.copy()
# 	for i in k:
# 		if i%3==0:
# 			s.add(i//3)
# 		if i%2==0:
# 			s.add(i//2)
# 		s.add(i-1)
# 		r.add(i)
# 	s=s-r
# print(result)