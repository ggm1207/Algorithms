def stars(string , n):
    if n == 1:
        print(string)
        return
    
    next_n = n//3
    next_s = [i for i in string]
    for i, _ in enumerate(string):
        if (i // next_n) % 3 == 1:
            next_s[i] = ' '
    next_s = ''.join(next_s)
    stars(string , next_n)
    stars(next_s , next_n)
    stars(string , next_n)

if __name__ == "__main__":
    n = int(input())
    string = "*"*n
    stars(string, n)

