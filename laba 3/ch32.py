x = 0.1
X = [-0.4, -0.1, 0.2, 0.5, 0.8]
Y = [-0.41152, -0.10017, 0.20136, 0.5236, 0.9273]
from sympy import *
c1, c2, c3= symbols('c1, c2, c3')
h=[]
h.append(0)
for i in range(1, len(X)):
    h.append(X[i]-X[i-1])
#print(h)

nm = len(X)-2
am = [0] * nm
bm = [0] * nm
cm = [0] * nm
bm[0] = 2*(h[1]+h[2])
cm[0] = h[2]
for i in range(1, nm-1):
    am[i] = h[i]
    bm[i] = 2*(h[i]+h[i+1])
    cm[i] = h[i+1]
am[nm-1]= h[nm-1]
bm[nm-1] = 2*(h[nm-1]+h[nm])
pch=[]
pch.append(3*((Y[2]-Y[1])/h[2]-(Y[1]-Y[0])/h[1]))
for i in range(3, nm+1):
    pch.append(3*((Y[i]-Y[i-1])/h[i]-(Y[i-1]-Y[i-2])/h[i-1]))
pch.append(3*((Y[nm+1]-Y[nm])/h[nm+1]-(Y[nm]-Y[nm-1])/h[nm]))

def progonka(a, b, c, d, n):
    p = [0] * n
    q = [0] * n
    p[0]=(-c[0]/b[0])
    q[0]=(d[0]/b[0])
    for i in range(1, n-1):
        p[i]=(-c[i]/(b[i] + a[i]*p[i-1]))
        q[i]=((d[i]-a[i]*q[i-1])/(b[i]+a[i]*p[i-1]))
    p[n-1]=0
    q[n-1]=(d[n-1]-a[n-1]*q[n-2])/(b[n-1]+a[n-1]*p[n-2])
    x = [0] * n
    x[n-1] = q[n-1]
    for i in range(1, n):
        x[n-1-i] = p[n-1-i]*x[n-i] + q[n-1-i]
    return x
c = progonka(am, bm, cm, pch, nm)
c.insert(0, 0)
#print(c)
a = []
for i in range(1, len(X)):
    a.append(Y[i-1])
#print(a)
b=[]
for i in range(1, len(X)-1):
    b.append((Y[i]-Y[i-1])/h[i]-h[i]*(c[i]+2*c[i-1])/3)
b.append((Y[len(X)-1]-Y[len(X)-2])/h[len(X)-1]-2*h[len(X)-1]*(c[len(X)-2])/3)
#print(b)
d=[]
for i in range(1, len(X)-1):
    d.append((c[i]-c[i-1])/(3*h[i]))
d.append(-c[len(X)-2]/(3*h[len(X)-1]))
#print(d)

def func(x, a, b, c, d, X):
    res = 0
    for i in range(1, len(X)):
        if x>X[i-1] and x<=X[i]:
            res = a[i-1]+b[i-1]*(x-X[i-1])+c[i-1]*(x-X[i-1])**2+d[i-1]*(x-X[i-1])**3
    return res
def funcstr(x, a, b, c, d, X):
    res = "f(x)="
    for i in range(1, len(X)):
        if x>X[i-1] and x<=X[i]:
            res += str(a[i-1])+"+"+str(b[i-1])+"(x"+str(X[i-1])+")"+str(c[i-1])+"(x"+str(X[i-1])+")^2+"+str(d[i-1])+"(x"+str(X[i-1])+")^3"
    return res
print("f(x*)=",func(x, a, b, c, d, X))
print(funcstr(x, a, b, c, d, X))
import matplotlib.pyplot as plt
import numpy as np
plt.plot(X, Y)
x = np.linspace(-0.399, 0.8, 50)
y=[]
for i in range(len(x)):
    y.append(func(x[i], a, b, c, d, X))
plt.plot(x,y)
plt.show()
