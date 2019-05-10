import string
alphabet = {}
for alpha in string.ascii_lowercase:
    alphabet[alpha] = -1
# print(alphabet)
if __name__ == "__main__":
    bj = input()
    cnt = 0
    for bet in bj:
        if alphabet[bet] == -1:
            alphabet[bet] = cnt
        cnt += 1
    print(" ".join(map(str,alphabet.values())))