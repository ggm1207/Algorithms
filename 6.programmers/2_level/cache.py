""" 캐시(https://programmers.co.kr/learn/courses/30/lessons/17680)
캐시크기(cacheSize)	도시이름(cities)	                                                    실행시간
3	                  [Jeju, Pangyo, Seoul, NewYork, LA, Jeju, Pangyo, Seoul, NewYork, LA]	50
3	                  [Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul]	21
2	                  [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	60
5	                  [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	52
2	                  [Jeju, Pangyo, NewYork, newyork]	16
0	                  [Jeju, Pangyo, Seoul, NewYork, LA]	25

당연히 lru 를 안다고 생각한게 화근..
계속 mfu 구현하고 왜 틀리나 고민하고 있었네
"""
def solution(cacheSize, cities):
  if cacheSize == 0:
    return 5 * len(cities)
  cities = map(lambda x: x.lower(), cities)
  caches = {}
  cur_size = 0
  cache_hit, cache_miss = 0, 0

  for i, city in enumerate(cities):
    # 1. city 가 caches 안에 있을 때
    if city in caches:
      cache_hit += 1
      caches[city] = i
    # 2. city 가 caches 안에 없을 때
    else:
      cache_miss += 1
      # 2-1. size가 다 찼을 때
      if cur_size == cacheSize:
        cache_sorted = sorted(list(caches.items()), key = lambda x : x[1])
        del caches[cache_sorted[0][0]]
        caches[city] = i
      # 2-2. size가 비었을 때 
      else:
        caches[city] = i
        cur_size += 1
  return cache_hit + cache_miss * 5

if __name__ == "__main__":
  cacheSize = 3
  cities = 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
  cities = map(lambda x: x.lower(), cities)
  if cacheSize == 0:
    print(5 * len(cities))

  caches = {}
  cur_size = 0
  cache_hit, cache_miss = 0, 0

  for i, city in enumerate(cities):
    # 1. city 가 caches 안에 있을 때
    print(city)
    if city in caches:
      cache_hit += 1
      caches[city] = i
    # 2. city 가 caches 안에 없을 때
    else:
      cache_miss += 1
      # 2-1. size가 다 찼을 때
      if cur_size == cacheSize:
        cache_sorted = sorted(list(caches.items()), key = lambda x : x[1])
        print(cache_sorted)
        del caches[cache_sorted[0][0]]
        caches[city] = i
      # 2-2. size가 비었을 때 
      else:
        caches[city] = i
        cur_size += 1
    print(caches)
  print(cache_hit + cache_miss * 5)