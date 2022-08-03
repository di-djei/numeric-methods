import math
print("kolvo strok")
n = int(input())
print("matrix")
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
print("pravaya chast")
b = list(map(float, input().split()))

def change(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    return A
l = [ [0]*n for i in range(n) ]
u=a
ch=0
for i in range(n):
    if u[i][i] == 0:
        if i !=n:
            change(u, i, i+1)
        else:
            change(u, i, 1)
        t=b[i]
        b[i]=b[i+1]
        b[i+1]=t
        ch += 1
print("matrix slau")
print(u)
for i in range(n):
    for j in range(i, n):
        l[j][i]=u[j][i]/u[i][i]
for k in range(1, n):
    for i in range(k-1, n):
        for j in range(i, n):
            l[j][i]=round(u[j][i]/u[i][i], 5)
    for i in range(k,n):
        for j in range(k-1, n):
            u[i][j]=round(u[i][j]-l[i][k-1]*u[k-1][j],5)
print("U")
print(u)
print("L")
print(l)

def solve(l, u, b):
    z =[0] * n
    z[0] = b[0]
    for i in range(1, n):
        sum = 0
        for j in range(i):
            sum = sum + l[i][j]*z[j]
        z[i]=b[i] - sum
    x = [0] * n
    x[n-1] = z[n-1]/u[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum = sum + u[i][j]*x[j]
        x[i]=(1/u[i][i])*(z[i]-sum)
    return x
print("otvet")
print(solve(l, u, b))

print("opredelitel")
opr = 1
for i in range(n):
    opr = opr*u[i][i]
if ch%2 != 0:
    opr = opr*(-1)
print(opr)

print("obratnaya")
obr = []
def obrat(l, u):
    for i in range(n):
        st = [0] * n
        st[i] = 1  
        obrst = solve(l, u, st)
        obr.append(obrst)
    trobr = [[obr[j][i] for j in range(len(obr))]for i in range(len(obr[0]))]
    return trobr
print(obrat(l, u))