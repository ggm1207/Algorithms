
if __name__ == "__main__":
    string = input()
    for i in range(len(string)//10+1):
        print(string[10*i:10*(i+1)])