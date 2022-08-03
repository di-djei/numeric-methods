print("method strelby")
from sympy import *
import numpy as np
def exact(x):
    return 3*x+exp(-2*x)
def f(x, y, y_der):
    return (4 * y - 4 * x * y_der) / (2 * x + 1)
def g(x, y, z):
    return z
def der1(x, y, x0):
    i = 0
    while i < len(x) - 1 and x[i + 1] < x0:
        i += 1
    return (y[i] - y[i-1]) / (x[i] - x[i-1])
def runge_kutta(f, g, a, b, h, y0, yd0):
    n=int((b-a)/h)
    xx = [i for i in np.arange(a, b + h, h)]
    x=[]
    for i in range(n):
        x.append(round(-2+h*i,3)+0.001)
    print(x)
    y=[y0]
    z=[yd0]
    for i in range(n-1):
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
        # print(y)
        # print(z)
    return x, y, z
def rrerror(res1, res2):
    err=[]
    for i in range(len(res1)):
        err.append(abs(res1[i]-res2[i]))
    return err
# def findnu(nu1, nu, prev, cur, b, delta, gamma, y1):
#     x = prev[0]
#     y = prev[1]
#     yd=der1(x, y, b)
#     phiprev = delta *y[-1]+ gamma * yd -y1
#     print(round(phiprev, 3))
#     x = cur[0]
#     y = cur[1]
#     yd = der1(x, y, b)
#     phicur = delta *y[-1]+ gamma * yd -y1
#     print(round(phicur, 5))
#     return (nu-(nu-nu1)/(phicur-phiprev) * (phicur))
# def fincheck(x, y, b, delta, gamma, y1, eps):
#     yd=der1(x, y, b)
#     return abs(delta*y[-1]+gamma*yd-y1)>eps
# def shooting(f, g, a, b, alpha, betta, delta, gamma, y0, y1, h, eps):
#     nup=0
#     nu=1
#     yd = (y0-alpha*nup)/betta
#     ansp=runge_kutta(f, g, a, b, h, nup, yd)[:2]
#     yd=(y0-alpha*nu)/betta
#     ans=runge_kutta(f, g, a, b, h, nu, yd)[:2]
#     while abs(nu-nup)>eps:
#         nu, nup=findnu(nup,nu,ansp,ans,b,delta,gamma,y1), nu
#         print("nu",round(nu,5))
#         ansp=ans
#         yd=(y0-alpha*nu)/betta
#         ans=runge_kutta(f, g, a, b, h, nu, yd)[:2]
#     return ans
def findnu(nu1, nu, prev, cur, b, delta, gamma, y1):
    x = prev[0]
    y = prev[1]
    yd=der1(x, y, b)
    phiprev = delta *y[-1]+ gamma * yd -y1
    print(round(phiprev, 3))
    x = cur[0]
    y = cur[1]
    yd = der1(x, y, b)
    phicur = delta *y[-1]+ gamma * yd -y1
    print(round(phicur, 5))
    return (nu-(nu-nu1)/(phicur-phiprev) * (phicur-1))
def fincheck(x, y, b, delta, gamma, y1, eps):
    yd=der1(x, y, b)
    return abs(delta*y[-1]+gamma*yd-y1)>eps
def shooting(f, g, a, b, alpha, betta, delta, gamma, y0, y1, h, eps):
    nup=1
    nu=0.8
    yd = (y0-alpha*nup)/betta
    ansp=runge_kutta(f, g, a, b, h, nup, yd)[:2]
    yd=(y0-alpha*nu)/betta
    ans=runge_kutta(f, g, a, b, h, nu, yd)[:2]
    while fincheck(ans[0], ans[1], b, delta, gamma, y1, eps):
        nu, nup=findnu(nup,nu,ansp,ans,b,delta,gamma,y1), nu
        print("nu",round(nu,5))
        ansp=ans
        yd=(y0-alpha*nu)/betta
        ans=runge_kutta(f, g, a, b, h, nu, yd)[:2]
    return ans
a=-2
b=0
alpha=2
betta=1
delta=0
gamma=1
y0=-9
y1=1
h=0.1
h2=0.2
eps=0.01
sh = shooting(f,g,a,b,alpha,betta,delta,gamma,y0,y1,h,eps)
print(sh)
import matplotlib.pyplot as plt
import numpy as np
plt.plot(sh[0], sh[1], color = 'b', label="h=0.1")
x = np.linspace(a, b, 30)
y=[]
for i in range(len(x)):
    y.append(exact(x[i]))
plt.plot(x,y, color = 'g')
plt.show()