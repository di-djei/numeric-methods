import numpy as np
import matplotlib.pyplot as plt
from sympy import *
def func(x):
    return log(x+1) - 2*x**2 + 1
def f1(x):
    return np.log(x+1)
def f2(x):
    return 2*x**2-1
def phi(x):
    return sqrt((log(x+1)+1)/2)
def d(f, a):
    return f.diff(x).subs(x, a)

x = np.arange(0,2,0.01)
plt.plot(x,f2(x))
plt.plot(x, f1(x))
plt.show()

x= Symbol('x')
res=[]
a = float(input())
b = float(input())
eps =float(input())
print("Prost iter")
res.append((a+b)/2)
iter = 0
q=0
a1=a
while a1<b+0.01:
    if abs(d(phi(x), a1)) > q:
        q = abs(d(phi(x), a1))
    a1 = round(a1+0.01, 3)
if q <= 1:
    print("1 koren")
while True:
    res.append(phi(res[iter]))
    iter+=1
    if q*abs(res[iter]-res[iter-1])/(1-q) < eps:
        break
print(round(res[iter], 3))
print(iter)
print("Newton")
n=[]
a1=a
while a1<b:
    if func(x).subs(x,a1)*func(x).diff(x).diff(x).subs(x, a1) > 0:
        n.append(a1)
        print("shod")
        break
    else:
        a1+=0.01
iter=0
while True:
    n.append(n[iter]-func(x).subs(x, n[iter])/d(func(x), n[iter]))
    iter+=1
    if abs(n[iter]-n[iter-1]) < eps:
        break
print(round(n[iter], 3))
print(iter)
