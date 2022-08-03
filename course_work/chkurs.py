import numpy as np
import matplotlib.pyplot as plt

def K(x, t):
    #return 1/(0.64*np.cos((x+t)/2)**2 - 1)
    #return x*t
    #return t*np.sin(x)
    return np.sqrt(x*t)
def g(x):
    #return 25 - 16*np.sin(x)**2
    #return np.sqrt(1-x**2)
    #return np.cos(x)
    return 5*x
def f(x):
    #return 17/2 + (128/17)*np.cos(2*x)
    #return np.sqrt(1-x**2)+x/2
    #return np.cos(x)-2*np.sin(x)/np.pi
    return 5*x+4*np.sqrt(x)

def Fredgolm(K, g, x, h, lamb):
    n = len(x)
    A = np.zeros((n,n))
    for i in range(n):
        if i != 0:
            A[i, 0] = -0.5*lamb*h*K(x[i], x[0])
        else:
            A[i, 0] = 1-0.5*lamb*h*K(x[i], x[0])
    for i in range(1, n-1):
        for j in range(n):
            if i==j:
                A[i, j] = 1 - lamb * h * K(x[i], x[j])
            else:
                A[i, j] = - lamb * h * K(x[i], x[j])
    for i in range(n):
        if i == n-1:
            A[i, n-1] = 1-lamb * 0.5 * h * K(x[i], x[n-1])
        else:
            A[i, n - 1] = - lamb * 0.5 * h * K(x[i], x[n - 1])
    return np.linalg.solve(A, g(x))
def error(x, y, f):
    error=0
    for i in range(len(x)):
        er=np.abs(f(x[i])-y[i])
        if er>error:
            error = er
    return error
#a=-np.pi
#b=np.pi
#lamb=3/(10*np.pi)
#a = 0
#b = 1
#lamb = 1
#a = 0
#b = np.pi
#lamb = 1/(2*np.pi)
a = 0
b = 1
lamb = 1

xex=np.arange(a, b, 0.001)
yex=f(xex)

h=float(input())
x=np.arange(a, b, h)
y=Fredgolm(K, g, x, h, lamb)
y[0]=f(x[0])
y[-1]=f(x[-1])
plt.plot(xex,yex, label="exact", color = "r")
plt.plot(x,y,label="Kvadratur", color = "b")
plt.title("h = "+str(h)+ " pogreshnost = "+str(error(x,y,f)))
plt.legend()
plt.show()