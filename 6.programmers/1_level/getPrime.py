import math

def solution(n):
    primes = [2]
    prime = [True for _ in range(n)]

    prime[0:2] = [False,False,True]
    prime[4::2] = list(map(lambda x : False, prime[4::2]))
    
    for i in range(2,int(math.floor(math.sqrt(n)))):
      # print(primes)
      if not prime[i]:
          continue
      else:
          flag = True
          for j in primes:
              if i % j == 0:
                  flag = False
                  break
          if flag: # prime[i]가 소수
              # print(i)
              prime[i] = True
              prime[i*2::i] = list(map(lambda x : False, prime[i*2::i]))
              primes.append(i)

    #print(prime)
    print(sum(prime))
    answer = sum(prime)
    return answer

n = int(input())
solution(n)