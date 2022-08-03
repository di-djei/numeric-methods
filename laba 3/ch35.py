def f(x):
    return 1/(x**2+4)
X0=-2
Xk=2
h1=1
h2=0.5
zn=0.78540

def pramoug(x, h):
    F=0
    for i in range(len(x)-1):
        F+=f((x[i]+x[i+1])/2)
    F*=h
    return F
def trap(y, h):
    n=len(y)-1
    return h*(y[0]/2 + sum([y[i] for i in range(1, n)]) + y[n]/2)
def Simpson(y, h):
    n=len(y)-1
    return h/3*(y[0]+sum([4*y[i] for i in range(1, n, 2)]) + 
    sum([2 * y[i] for i in range(2, n-1, 2)]) + y[n])
import numpy as np
x1=np.arange(X0,Xk+h1,h1)
x2=np.arange(X0,Xk+h2,h2)
y1=[f(x) for x in x1]
y2=[f(x) for x in x2]
print("for h1 = ", h1)
p1=pramoug(x1, h1)
t1=trap(y1, h1)
s1=Simpson(y1, h1)
print("method pramoug: ", p1)
print("method trap: ", t1)
print("method Simpson: ", s1)

print("for h2 =", h2)
p2=pramoug(x2, h2)
t2=trap(y2, h2)
s2=Simpson(y2, h2)
print("method pramoug: ",p2)
print("method trap: ", t2)
print("method Simpson: ", s2)

def runge(zn1, zn2, zn):
    ut=zn1+(zn1-zn2)/((h2/h1)**2-1)
    oshibka=abs(zn1+(zn1-zn2)/((h2/h1)**2-1)-zn)
    return ut, oshibka

print("utochnenie y oshibka po Runge-Romberg-Richardson")
print("pramoug: ",runge(p1, p2, zn))
print("trap: ",runge(t1, t2, zn))
print("Simpson: ",runge(s1, s2, zn))
