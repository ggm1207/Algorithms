""" 캐시(https://programmers.co.kr/learn/courses/30/lessons/17680)
캐시크기(cacheSize)	도시이름(cities)	                                                    실행시간
3	                  [Jeju, Pangyo, Seoul, NewYork, LA, Jeju, Pangyo, Seoul, NewYork, LA]	50
3	                  [Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul]	21
2	                  [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	60
5	                  [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome]	52
2	                  [Jeju, Pangyo, NewYork, newyork]	16
0	                  [Jeju, Pangyo, Seoul, NewYork, LA]	25
"""
def solution(cacheSize, cities):
  if cacheSize == 0:
    return 5 * len(cities)
  cache_hit = cache_miss = size = 0
  caches = {}
  cities = list(map(lambda x : x.lower(), cities))

  mazino = 0

  for city in cities:
    # print(caches)

    if city in caches:
      cache_hit += 1
      caches[city] += 1
      continue
    else:
      cache_miss += 1
      if size == cacheSize:
        del_city = sorted(list(caches.items()), key = lambda x: x[1])
        del_v = del_city[0][1]
        del_city = list(filter(lambda x : x[1] == del_v, del_city))
        # print(cities[mazino:])
        # print(del_city)
        # print()
        counts = [cities[mazino:].index(d_c) for d_c, v in del_city]
        # print(counts)
        d_c = del_city[counts.index(min(counts))][0]
        n_list = list(caches.keys())
        countss = [cities[mazino:].index(n) for n in n_list]
        
        del caches[d_c]
        # print('n_list:', n_list)
        mazino += cities[mazino:].index(n_list[countss.index(min(countss))])
      else:
        size += 1
      caches[city] = 1

  return cache_hit + cache_miss * 5

if __name__ == "__main__":
  cacheSize = 3
  cities = 	["Jeju", "Pangyo", "Seoul", "NewYork", "NewYork","NewYork","NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
  print(solution(cacheSize, cities))