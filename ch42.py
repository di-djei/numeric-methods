print("Konechno-raznost method")
from sympy import *
def exact(x):
    return 3*x+exp(-2*x)
import matplotlib.pyplot as plt
import numpy as np
def p(x):
    return 4*x/(2*x+1)
def q(x):
    return -4/(2*x+1)
def f(x):
    return 0
h1=0.05
h2=0.1
a=-2
b=0
y0=-9
y1=1
def knr(h, f, p, q):
    x = []
    s=2/h
    for i in range(int(s)+1):
        if -2+h*i!=-0.5:
            x.append(round(-2+h*i,3))
        else:
            x.append(-0.501)
    n=len(x)-2
    am = [0] + [1 - p(x[i]) * h / 2 for i in range(0, n - 1)] + [1-p(x[n+1])*h/2]
    bm=[-1/h] + [q(x[i]) * h ** 2 - 2 for i in range(0, n - 1)] + [-2-q(x[n+1])*h**2]
    cm=[1/h+2] + [1 + p(x[i]) * h / 2 for i in range(0, n - 1)] + [0]
    pch=[y0] + [f(x[i]) * h ** 2 for i in range(0, n - 1)] + [f(x[n+1]) * h ** 2-(1+p(x[n+1])*h/2)*y1]
    c = progonka(am, bm, cm, pch, n+1)
    c.append(y1)
    return c, x
#print(am, bm, cm, pch)
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
c1 = knr(h1, f, p, q)[0]
print(c1)
c2 = knr(h2, f, p, q)[0]
print(c2)

def runge(res1, res2):
    err=[]
    for i in range(len(res2)):
        err.append(abs(res1[i*2]-res2[i])**2)
    return sum(err)**0.5
def exacterror(res, ex):
    err=[]
    for i in range(len(res)):
        err.append(abs(res[i]-ex[i])**2)
    return sum(err)**0.5
print("pogresh RR: ", runge(c1, c2))
c11=[]
for i in range(len(c1)):
    if i%2==1:
        c11.append(c1[i])

x = np.linspace(-2, 0, 30)
y=[]
for i in range(len(x)):
    y.append(exact(x[i]))
    
t=[]
for i in range(len(knr(h2, f, p, q)[1])):
    t.append(exact(knr(h2, f, p, q)[1][i]))
print("pogresh tochn(",h1,"): ", exacterror(c11, t)) 
print("pogresh tochn(",h2,"): ", exacterror(c2, t))  

plt.plot(knr(h1, f, p, q)[1],c1, color = 'r', label="h=0.05")
plt.plot(knr(h2, f, p, q)[1],c2, color = 'b', label="h=0.1")

plt.plot(x,y, color = 'g', label="exact")
plt.legend()
plt.show()