def X_U_Y(X,Y):
    X = X[:-1]
    Y = Y[:-1]
    XUY = []
    for i in X:
        if i in Y:
            continue
        else:
            XUY.append(i)
    print(XUY + Y + [0])

def X_n_Y(X,Y):
    X = X[:-1]
    Y = Y[:-1]
    XnY = []
    for i in X:
        if i in Y:
            XnY.append(i)
    print(XnY + [0])

def X_Y(X,Y):
    X = X[:-1]
    Y = Y[:-1]
    X_Y = []
    for i in X:
        if i in Y:
            continue
        else:
            X_Y.append(i)
    print(X_Y + [0])

def XAY(X,Y):
    X = X[:-1]
    Y = Y[:-1]
    XAY = []
    for i in X:
        if i in Y:
            Y.remove(i)
        else:
            XAY.append(i)
    print(XAY + Y + [0])

if __name__ == "__main__":
    A = [1,3,4,2,0]
    B = [4,3,6,7,0]
    X_U_Y(A,B)
    X_n_Y(A,B)
    X_Y(A,B)
    XAY(A,B)