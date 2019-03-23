def XEY(X,E):
    X = X[:-1]
    if E in X:
        print('E 는 X에 속해있습니다.')
    else:
        print('E 는 X에 속해있지않습니다.')
            
if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10,0]
    B = 15
    XEY(A,B)