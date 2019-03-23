def XCY(X,Y):
    istrue = True
    X = X[:-1]
    Y = Y[:-1]
    for i in X:
        if i in Y:
            continue
        else:
            istrue = False
    if istrue:
        print('속해있습니다.')
    else:
        print('속해있지않습니다.')
    

if __name__ == "__main__":
    A = [4,3,0]
    B = [4,3,6,7,0]
    XCY(A,B)