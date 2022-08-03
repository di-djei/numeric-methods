import math
print("Kolvo uravneniy")
n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
print("chisla v ur")
a[0] = 0
b[0], c[0] = map(float,input().split())
for i in range(1, n-1):
    a[i], b[i], c[i] = map(float,input().split())
a[n-1], b[n-1] = map(float,input().split())
c[n-1] = 0
print("pravaya chast")
d = list(map(float, input().split()))

ust = True
countust = 0
count2 = 0
for i in range(1, n-2):
    if a[i] == 0:
        ust = False
    if c[i] == 0:
        ust = False
for i in range(n):
    if abs(b[i])>=abs(a[i])+abs(c[i]):
        countust +=1
    if abs(b[i])>=abs(a[i])+abs(c[i]):
        count2 +=1
if countust != n:
    ust = False
if count2 == 0:
    ust = False
if ust == True:
    print("ustoychivo")
else:
    print("ne ustoychivo")

p = [0] * n
q = [0] * n
p[0]=(-c[0]/b[0])
q[0]=(d[0]/b[0])
for i in range(1, n-1):
    p[i]=(-c[i]/(b[i] + a[i]*p[i-1]))
    q[i]=((d[i]-a[i]*q[i-1])/(b[i]+a[i]*p[i-1]))
p[n-1]=0
q[n-1]=(d[n-1]-a[n-1]*q[n-2])/(b[n-1]+a[n-1]*p[n-2])
print("Q = ", p)
print("P = ", q)

x = [0] * n
x[n-1] = q[n-1]
for i in range(1, n):
    x[n-1-i] = p[n-1-i]*x[n-i] + q[n-1-i]
print("X = ", x)