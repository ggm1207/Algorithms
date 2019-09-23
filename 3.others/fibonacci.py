from functools import lru_cache
from timeit import default_timer as time
from sys import setrecursionlimit
setrecursionlimit(1000000)

def timer(func):
    def wrapper(*args, **kargs):
        s = time()
        result = func(*args, **kargs)
        print(func.__name__ , "'s time: ", time() - s)
        return result
    return wrapper


@timer
def dp_fibo_with_arr(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a , b = b , a + b
    return b

# 3까지는 해야 dp 처럼 작동 2 하면 재귀의 수렁으로 들어감
# cache 탐색 시간이 추가 되어서 real dp 보다 살짝 느린 듯.

@lru_cache(maxsize=3) 
def dp_fibo_with_lru(n): 
    if n < 2:
        return n
    return dp_fibo_with_lru(n-1) + dp_fibo_with_lru(n-2)


n = int(input())

dp_fibo_with_arr(n)
s = time()
for i in range(2, n+1):
    dp_fibo_with_lru(i)
print(dp_fibo_with_lru.__name__ , "'s time: ", time() - s)
print(dp_fibo_with_lru.cache_info())