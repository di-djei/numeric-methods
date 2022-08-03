from sympy import *
def f1(x, y):
    return x**2+y**2-9
def f2(x, y):
    return x-exp(y)+3
def det(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def phi1(x, y):
    return sqrt(9-y**2)
def phi2(x, y):
    return log(x+3)
    
x, y = symbols('x y')
p1 = plot_implicit(f1(x, y), (x, 0, 3), (y, 0, 3), show=False)
p2 = plot_implicit(f2(x, y), (x, 0, 3), (y, 0, 3), show=False)
p1.append(p2[0])
p1.show()

x1 = float(input())
y1 = float(input())
eps =float(input())
print("Newton")
xn = []
yn = []
xn.append(x1)
yn.append(y1)
iter = 0
while True:
    dx1 = f1(x,y).diff(x).subs([(x, xn[iter]), (y, yn[iter])])
    dy1 = f1(x,y).diff(y).subs([(x, xn[iter]), (y, yn[iter])])
    dx2 = f2(x,y).diff(x).subs([(x, xn[iter]), (y, yn[iter])])
    dy2 = f2(x,y).diff(y).subs([(x, xn[iter]), (y, yn[iter])])
    j = [[dx1, dy1], [dx2, dy2]]
    a1 = [[0, dy1], [0, dy2]]
    a1[0][0] = f1(x,y).subs([(x, xn[iter]), (y, yn[iter])])
    a1[1][0] = f2(x,y).subs([(x, xn[iter]), (y, yn[iter])])
    a2 = [[dx1, 0], [dx2, 0]]
    a2[0][1] = f1(x,y).subs([(x, xn[iter]), (y, yn[iter])])
    a2[1][1] = f2(x,y).subs([(x, xn[iter]), (y, yn[iter])])
    xn.append(xn[iter]-det(a1)/det(j))
    yn.append(yn[iter]-det(a2)/det(j))
    iter+=1
    if max(xn[iter]-xn[iter-1], yn[iter]-yn[iter-1])<eps:
        break
print(round(xn[iter], 5))
print(round(yn[iter], 5))
print(iter)
print("Prost iter")
iter = 0
xp = []
yp=[]
xp.append(x1)
yp.append(y1)
q1 = abs(phi1(x, y).diff(x).subs([(x, x1), (y, y1)]))+abs(phi1(x, y).diff(y).subs([(x, x1), (y, y1)]))
q2 = abs(phi2(x, y).diff(x).subs([(x, x1), (y, y1)]))+abs(phi2(x, y).diff(y).subs([(x, x1), (y, y1)]))
q=max(q1, q2)
if q<1:
    print("shod")
while True:
    xp.append(phi1(x, y).subs([(x, xp[iter]), (y, yp[iter])]))
    yp.append(phi2(x, y).subs([(x, xp[iter]), (y, yp[iter])]))
    iter+=1
    if abs(q*max(xp[iter]-xp[iter-1], yp[iter]-yp[iter-1]))/(1-q)<eps:
        break
print(round(xp[iter], 5))
print(round(yp[iter], 5))
print(iter)