import math
print("kolvo strok")
n = int(input())
print("matrix")
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
print("pravaya chast")
b = list(map(float, input().split()))
print("epsilon")
eps=float(input())

betta = [0] * n
alpha = [ [0]*n for i in range(n) ]
for i in range(n):
    betta[i]=b[i]/a[i][i]
    for j in range(n):
        alpha[i][j] = -a[i][j]/a[i][i]
for i in range(n):
    alpha[i][i] = 0
#print("priveden vid")
#print("Alpha = ",alpha)
#print("Betta = ",betta)
maxes = [0] *n
for i in range(n):
    m=0
    for j in range(n):
        m+=abs(alpha[i][j])
    maxes[i]=m
alf=max(maxes)
if alf < 1:
    print("shod")
else:
    print("ne shod")
def matrstr(a, b):
    pr = [0] *n
    for i in range(len(b)):
        for j in range(len(b)):
            pr[i]+=a[i][j]*b[j]
    return pr
def summa(a, b):
    sum = [0]*n
    for i in range(len(a)):
        sum[i] = a[i]+b[i]
    return sum
def normax(x, y):
    xx = [0] *n
    for i in range(n):
        m=0
        xx[i]=abs(x[i]-y[i])
    normx = max(xx)
    return normx

x = []
x.append(betta)
iter = 0
while True:
    x.append(summa(betta,matrstr(alpha,x[iter])))
    normx = normax(x[iter+1], x[iter])
    myeps = (alf/(1-alf))*normx
    iter +=1
    if normx < eps:
        break
print("prost iteratsi")
print("X = ",x[-1])
print("i = ",iter)

#Zeidel
print("Zeidel")
z = []
z.append(betta)
iter = 0
while True:
    z.append([0] * n)
    for i in range(n):
        s=0
        for j in range(n):
            if j < i:
                s+= alpha[i][j] * z[iter+1][j]
            elif j > i:
                s+= alpha[i][j] * z[iter][j]
        z[iter+1][i]=betta[i]+s
    meps = normax(z[iter+1], z[iter])
    iter +=1
    if meps < eps:
        break
print("X = ", z[-1])
print("i = ",iter)