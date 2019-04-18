import sys

def primes_up_to_good(n:int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]], seive

if __name__ == "__main__":
    nums = []
    while(1):
        n = int(sys.stdin.readline())
        if not n:
            break
        nums.append(n)
    
    prime_list, is_prime = primes_up_to_good(max(nums))
    print(is_prime[:20])
    
    flag = False
    for i in nums:
        for a in prime_list:
            b = i-a
            if is_prime[b]:
                msg = '{} = {} + {}\n' .format(i,a,b)
                sys.stdout.write(msg)
                flag = True
                break
    if not flag:
        print("Goldbach's conjecture is wrong.")