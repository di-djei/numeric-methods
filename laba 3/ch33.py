X=[-0.7, -0.4, -0.1, 0.2, 0.5, 0.8]
Y=[-0.7754, -0.41152, -0.10017, 0.20136, 0.5236, 0.9273]
n= len(X)
print("1 stepen")
sumx = sum(X)
sumy = sum(Y)
xx = 0
for i in range(n):
    xx+=X[i]**2
xy = 0
for i in range(n):
    xy+=X[i]*Y[i]
a=[0]*2
a[0]=(sumy*xx-xy*sumx)/((n)*xx-sumx**2)
a[1]=(sumy*sumx-(n)*xy)/(sumx**2-(n)*xx)
print("F1(x) = ", a[0], "+", a[1], "x")
F1=[0]*n
def func(a, x):
    return a[0]+a[1]*x
for i in range(n):
    F1[i]=func(a, X[i])
p=0
for i in range(n):
    p+=(F1[i]-Y[i])**2
print("oshibka")
print(p)

print("2 stepen")
xxx=0
for i in range(n):
    xxx+=X[i]**3
xxxx=0
for i in range(n):
    xxxx+=X[i]**4
xxy=0
for i in range(n):
    xxy+=Y[i]*X[i]**2
a1=[0]*3
a1[2]=(n*xx*xxy-n*xxx*xy-sumx**2*xxy+sumx*sumy*xxx+sumx*xx*xy-sumy*xx**2)/(n*xx*xxxx-n*xxx**2-sumx**2*xxxx+2*sumx*xx*xxx-xx**3)
a1[1]=(sumx*(xx*a1[2]-sumy)-n*(xxx*a1[2]-xy))/(n*xx-sumx**2)
a1[0]=-(sumx*a1[1]+xx*a1[2]-sumy)/n
print("F2(x) = ", a1[0], "+", a1[1], "x +", a1[2],"x^2")
F2=[0]*n
def func2(a1, x):
    return a1[0]+a1[1]*x+a1[2]*x**2
for i in range(n):
    F2[i]=func2(a1, X[i])
p1=0
for i in range(n):
    p1+=(F2[i]-Y[i])**2
print("oshibka")
print(p1)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(X, Y, color = 'b', label="points")
x = np.linspace(-0.7, 0.8, 50)
y=[]
for i in range(len(x)):
    y.append(func(a, x[i]))
plt.plot(x,y, color = 'g', label="1 stepen")
y=[]
for i in range(len(x)):
    y.append(func2(a1, x[i]))
plt.plot(x,y, color = 'r', label="2 stepen")
plt.legend()
plt.show()