def XY(U,X):
    U = U[:-1]
    X = X[:-1]
    NOTX = []
    for i in U:
        if i in X:
            continue
        else:
            NOTX.append(i)
    print(NOTX)
            
if __name__ == "__main__":
    U = [1,2,3,4,5,6,7,8,9,10,0]
    B = [4,3,6,7,0]
    XY(U,B)