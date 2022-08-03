from tkinter import Y
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
def exact(x):
    return (exp(x)+exp(-x)-1)*exp(x**2)
def f(x, y, yd):
    return 4*x*yd-(4*x**2-3)*y+exp(x**2)
def g(x, y, z):
    return z
y0=1
yd0=0
h=0.1
h1=0.2
a=0
b=1

def exactes(f, a, b, h):
    x = [i for i in np.arange(a, b + h, h)]
    y = [f(i) for i in x]
    return x, y
def euler(f, g, a, b, h, y0, yder):
    n=int((b-a)/h)
    x = [i for i in np.arange(a, b + h, h)]
    y=[]
    y.append(y0)
    z=yder
    for i in range(n):
        z+=h*f(x[i],y[i], z)
        y.append(y[i]+h*g(x[i], y[i], z))
    return x, y
def runge_kutta(f, g, a, b, h, y0, yd0):
    n=int((b-a)/h)
    x = [i for i in np.arange(a, b + h, h)]
    y=[y0]
    z=[yd0]
    for i in range(n):
        K1=h*g(x[i],y[i],z[i])
        L1=h*f(x[i],y[i],z[i])
        K2=h*g(x[i]+0.5*h,y[i]+0.5*K1,z[i]+0.5*L1)
        L2=h*f(x[i]+0.5*h,y[i]+0.5*K1,z[i]+0.5*L1)
        K3=h*g(x[i]+0.5*h,y[i]+0.5*K2,z[i]+0.5*L2)
        L3=h*f(x[i]+0.5*h,y[i]+0.5*K2,z[i]+0.5*L2)
        K4=h*g(x[i]+h,y[i]+K3,z[i]+L3)
        L4=h*f(x[i]+h,y[i]+K3,z[i]+L3)
        delta_y=(K1+2*K2+2*K3+K4)/6
        delta_z=(L1+2*L2+2*L3+L4)/6
        y.append(y[i]+delta_y)
        z.append(z[i]+delta_z)
    return x, y, z
def adams(f, g, x, y, z, h):
    n = len(x)-1
    x=x[:4]
    y=y[:4]
    z=z[:4]
    for i in range(3, n):
        zi=z[i]+h*(55*f(x[i],y[i],z[i])-
            59*f(x[i-1],y[i-1],z[i-1])+
            37*f(x[i-2],y[i-2],z[i-2])-
            9*f(x[i-3],y[i-3],z[i-3]))/24
        z.append(zi)
        yi=y[i]+h*(55*g(x[i],y[i],z[i])-
            59*g(x[i-1],y[i-1],z[i-1])+
            37*g(x[i-2],y[i-2],z[i-2])-
            9*g(x[i-3],y[i-3],z[i-3]))/24
        y.append(yi)
        x.append(x[i]+h)
    return x, y
def RRerror(res1, res2, h1, h2, m):
    k = h1/h2
    err=[]
    for i in range(len(res2)):
        err.append(abs(res1[i*2]-res2[i])**2)
    if m =="e":
        er=sqrt(sum(err))/(k**1-1)
    else:
        er=(sum(err)**0.5)/(k**4-1)
    return er
            
def exacterror(res, ex):
    err=[]
    for i in range(len(res)):
        err.append(abs(res[i]-ex[i])**2)
    return sum(err)**0.5
ex=exactes(exact, a, b, h)[1]
print("Euler")
print(exactes(exact, a, b, h)[1])
print("Runge Kutta")
print(euler(f, g, a, b, h, y0, yd0)[1])
print(runge_kutta(f, g, a, b, h, y0, yd0)[1])
ad1=adams(f, g, runge_kutta(f, g, a, b, h, y0, yd0)[0],
    runge_kutta(f, g, a, b, h, y0, yd0)[1],
    runge_kutta(f, g, a, b, h, y0, yd0)[2], h)
ad2=adams(f, g, runge_kutta(f, g, a, b, h1, y0, yd0)[0],
    runge_kutta(f, g, a, b, h1, y0, yd0)[1],
    runge_kutta(f, g, a, b, h1, y0, yd0)[2], h1)
print("Adams")
print(ad1[1])
print("Error Runge Romberg (h=0.1 and h=0.2)")
print(RRerror(euler(f, g, a, b, h, y0, yd0)[1],
    euler(f, g, a, b, h1, y0, yd0)[1],h, h1,"e"))
print(RRerror(runge_kutta(f, g, a, b, h, y0, yd0)[1],
    runge_kutta(f, g, a, b, h1, y0, yd0)[1],h, h1,"r"))
print(RRerror(ad1[1], ad2[1],h, h1,"a"))
print("Exact error")
print(exacterror(euler(f, g, a, b, h, y0, yd0)[1], ex))
print(exacterror(runge_kutta(f, g, a, b, h, y0, yd0)[1], ex))
print(exacterror(ad1[1], ex))

plt.title("h=0.1")
plt.plot(euler(f, g, a, b, h, y0, yd0)[0],
    euler(f, g, a, b, h, y0, yd0)[1], color = 'r', label="euler")
plt.plot(runge_kutta(f, g, a, b, h, y0, yd0)[0],
    runge_kutta(f, g, a, b, h, y0, yd0)[1], color = 'b', label="runge kutta")
plt.plot(ad1[0], ad1[1], color = 'y', label = "adams")
x = np.linspace(0, 1, 30)
y=[]
for i in range(len(x)):
    y.append(exact(x[i]))
plt.plot(x,y, color = 'g', label="exact")
plt.legend()
plt.show()

plt.title("h=0.2")
plt.plot(euler(f, g, a, b, h1, y0, yd0)[0],
    euler(f, g, a, b, h1, y0, yd0)[1], color = 'r', label="euler")
plt.plot(runge_kutta(f, g, a, b, h1, y0, yd0)[0],
    runge_kutta(f, g, a, b, h1, y0, yd0)[1], color = 'b', label="runge kutta")
plt.plot(ad2[0], ad2[1], color = 'y', label = "adams")
x = np.linspace(0, 1, 30)
y=[]
for i in range(len(x)):
    y.append(exact(x[i]))
plt.plot(x,y, color = 'g', label="exact")
plt.legend()
plt.show()