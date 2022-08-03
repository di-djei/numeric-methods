print("method strelby")
from sympy import *
import numpy as np
def exact(x):
    return 3*x+exp(-2*x)
def f(x, y, y_der):
    return (4 * y - 4 * x * y_der) / (2 * x + 1)
def g(x, y, z):
    return z
def runge_kutta(f, g, a, b, h, y0, yd0):
    n=int((b-a)/h)
    x = [i for i in np.arange(a+0.001, b + h+0.001, h)]
    y=[y0]
    z=[yd0]
    for i in range(n):
        K1=round(h*g(x[i],y[i],z[i]),5)
        L1=round(h*f(x[i],y[i],z[i]),5)
        K2=round(h*g(x[i]+0.5*h,y[i]+0.5*K1,z[i]+0.5*L1),5)
        L2=round(h*f(x[i]+0.5*h,y[i]+0.5*K1,z[i]+0.5*L1),5)
        K3=round(h*g(x[i]+0.5*h,y[i]+0.5*K2,z[i]+0.5*L2),5)
        L3=round(h*f(x[i]+0.5*h,y[i]+0.5*K2,z[i]+0.5*L2),5)
        K4=round(h*g(x[i]+h,y[i]+K3,z[i]+L3),5)
        L4=round(h*f(x[i]+h,y[i]+K3,z[i]+L3),5)
        delta_y=(K1+2*K2+2*K3+K4)/6
        delta_z=(L1+2*L2+2*L3+L4)/6
        y.append(y[i]+delta_y)
        z.append(z[i]+delta_z)
    return y
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
def shooting(f, g, a, b, y0, y1, h, eps):
    nu=[1, 0.8]
    rk=[]
    rk.append(runge_kutta(f,g,a,b,h,(y0-nu[0])/2,nu[0])[-1])
    rk.append(runge_kutta(f,g,a,b,h,(y0-nu[1])/2,nu[1])[-1])
    # print(rk)
    i=0
    phi=[]
    while True:
        nu.append(nu[i+1]-(nu[i+1]-nu[i])/(rk[i+1]-rk[i])*(rk[i+1]-y1))
        rk.append(runge_kutta(f,g,a,b,h,(y0-nu[i+2])/2,nu[i+2])[-1])
        phi.append(rk[i+2]-y1)
        if abs(phi[i])<eps:
            break
        i+=1
    return nu, rk, phi
a=-2
b=0
y0=-9
y1=1
h=0.1
h1=0.2
eps=0.0001
sh = shooting(f,g,a,b,y0,y1,h,eps)
# print(sh)
point=runge_kutta(f,g,a,b,h,(y0-sh[0][-1])/2,sh[0][-1])
print(point)
sh1 = shooting(f,g,a,b,y0,y1,h1,eps)
# print(sh1)
point1=runge_kutta(f,g,a,b,h1,(y0-sh1[0][-1])/2,sh1[0][-1])
# print(point1)
print("RRerror")
print(runge(point, point1))
print("exact error")
c11=[]
for i in range(len(point)):
    if i%2==0:
        c11.append(point[i])
t=[]
x = np.linspace(a, b, len(point))
for i in range(len(point)):
    t.append(exact(x[i]))
print("pogresh tochn(",h,"): ", exacterror(point, t)/5)
t=[]
x = np.linspace(a, b, len(point1))
for i in range(len(point1)):
    t.append(exact(x[i]))
print("pogresh tochn(",h1,"): ", exacterror(point1, t))
import matplotlib.pyplot as plt
import numpy as np
x = [i for i in np.arange(a, b + h, h)]
plt.plot(x, point, color = 'r', label="h=0.1")
x = [i for i in np.arange(a, b + h1, h1)]
plt.plot(x, point1, color = 'b', label="h=0.2")
x = np.linspace(a, b, 30)
y=[]
for i in range(len(x)):
    y.append(exact(x[i]))
plt.plot(x,y, color = 'g')
plt.show()