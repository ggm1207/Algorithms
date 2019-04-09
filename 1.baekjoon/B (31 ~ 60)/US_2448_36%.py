def stars(string, count): # arr 접근 가능
    if count > N:
        return
    
    print(string)
    stars(string, count+1)
    

        
def only_star(n, count):
    if arr[count-1][n] == "*":
        return
    else:
        arr[count-1][n] = "*"
    return

if __name__ == "__main__":
    N = int(input())
    # [n - 1] * [n - 1]
    string = " "*(N-1) + "*" + " "*(N-1)
    string = "*" 
    print(string)
    stars(string,1)
    
