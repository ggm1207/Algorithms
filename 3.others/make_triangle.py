def Find_triangle(number):
    num = number
    Short_segment = 0
    long_segment = 0
    last_segment = 0
    count = 0
    for i in range(1 , int(num/3)):
        for j in range(int((num - i)/2) , n):
            last_segment = n - i - j
            if j < i + last_segment:
                count += 1
    print(count)


if __name__ == "__main__":
    n = int(input())
    Find_triangle(n)
