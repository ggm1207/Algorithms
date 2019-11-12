from collections import defaultdict
import sys
import random

def solution(stones, k):
    m_v, min_v = 0, 200000001
    i = 0
    while(i < len(stones) -k + 1):
        m_v = max(stones[i:i+k])
        min_v = min(min_v, m_v)
        i = i + k - stones[i:i+k][::-1].index(m_v)

    return min_v

if __name__ == "__main__":
    random.seed(1000)
    stones = [random.randint(1,10000) for i in range(200000)]
    k = 5000

    m_v, min_v = 0, 200000001
    i = 0
    while(i < len(stones) -k + 1):
        m_v = max(stones[i:i+k])
        min_v = min(min_v, m_v)
        i = i + k - stones[i:i+k][::-1].index(m_v)

    # for i in range(len(stones) -k + 1):
    #     m_v = max(stones[i:i+k])
    #     min_v = min(min_v, m_v)
    # stones_list = [max(stones[i:i+k]) for i in range(len(stones) - k + 1)]

    answer = min_v
    print(answer)