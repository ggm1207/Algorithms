if __name__ == "__main__":
    A , B =input().split()
    list1 = sorted([A[::-1],B[::-1]])
    print(list1[1])
    