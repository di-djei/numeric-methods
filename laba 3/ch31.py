X1 = [-0.4, -0.1, 0.2, 0.5]
x = 0.1
from sympy import *
def f(x):
    return asin(x)
def omega(x, X):
    om=1
    for i in range(len(X)):
        if x!= X[i]:
            om = om*(x-X[i])
    return om
def Lagranzstr(X):
    Lagran = "L(x) = "
    for i in range(len(X)):
        if f(X[i])/omega(X[i], X) > 0 and i!=0:
            Lagran += "+"
        Lagran += str(f(X[i])/omega(X[i], X))
        for j in range(len(X)):
            if i!=j:
                if X[j]>0:
                    Lagran += "(x-"+str(X[j])+")"
                else:
                    Lagran += "(x"+str(X[j])+")"
    return Lagran
def Lagranz(X, x):
    Lagran = 0
    for i in range(len(X)):
        slag= f(X[i])/omega(X[i], X)
        for j in range(len(X)):
            if i!=j:
                slag *= (x-X[j])
        Lagran+=slag
    return Lagran
def konrazn(X):
    fi = [ [0]*len(X) for i in range(len(X)) ]
    for i in range(len(X)):
            fi[0][i] = f(X[i])
    for i in range(1, len(X)):
        for j in range(len(X)-i):
            fi[i][j] = round((fi[i-1][j+1] - fi[i-1][j])/(X[j+i]-X[j]), 5)
    return fi
def Newtonstr(X, fi):
    Newton = "P(x) = "
    for i in range(len(X)):
        if fi[i][0] > 0 and i!=0:
            Newton += "+"
        if fi[i][0] !=0:
            Newton+=str(fi[i][0])
            for j in range(i):
                if X[j]>0:
                    Newton += "(x-"+str(X[j])+")"
                elif X[j]<0:
                    Newton += "(x"+str(X[j])+")"
                else:
                    Newton += "x"
    return Newton
def Newton(X, x, fi):
    Newt = 0
    for i in range(len(X)):
        slag= fi[i][0]
        for j in range(i):
            slag *= (x-X[j])
        Newt+=slag
    return Newt
print("with X1")
print("Lagranz")
print(Lagranzstr(X1))
print("L("+str(x)+") =", Lagranz(X1, x))
print("y(", x, ") =", f(x))
print("pogresh = ", abs(f(x) - Lagranz(X1, x)))

print("Newton")
fi = konrazn(X1)
print(Newtonstr(X1, fi))
print("P("+str(x)+") =", Newton(X1, x, fi))
print("y(", x, ") =", f(x))
print("pogresh = ", abs(f(x) - Newton(X1, x, fi)))
