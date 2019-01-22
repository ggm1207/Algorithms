if __name__ == "__main__":
    input()
    lists = []
    lists = input().split()
    print(lists)
    lists = *map(lambda x : int(x), lists)
    print(lists)
    print('%d %d' %(min(lists),max(lists)))
