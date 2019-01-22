import sys

if __name__ == "__main__":
    n , m = map(int , input().split(' '))
    print(n // m) # int(n/m) -> python이 Big Integer는 디폴트로 지원해도 BigDecmal은
                  # 따로 쓰지 않는 이상 지원하지 않는다. 그러므로 // 사용.
                  # 너무 큰 수를 분모로 할 경우 / 는 터짐.
    print(n % m, end = '')