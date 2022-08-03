import math
print("kolvo strok")
n = int(input())
print("matrix")
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print("epsilon")
eps=float(input())

def maxnotdiag(m):
    maxnd = abs(m[0][1])
    maxi = 0
    maxj= 1
    for i in range(n):
        for j in range(i):
            if abs(m[i][j]) > maxnd:
                maxnd=m[i][j]
                maxi=i
                maxj=j
    return maxnd, maxi, maxj
def trans(m):
    res = [[m[j][i] for j in range(n)] for i in range(n)]
    return res
def proizv(m1, m2):
    res = [ [0]*n for i in range(n) ]
    for i in range(n):
        for j in range(n):       
            res[i][j] = round(sum(m1[i][k] * m2[k][j] for k in range(n)), 3)
    return res
def matrvr(mi, mj, uu):
    if uu[mi][mi] == uu[mj][mj]:
        fi = math.pi/4
    else:
        fi = 0.5 * math.atan(2*uu[mi][mj]/(uu[mi][mi] - uu[mj][mj]))
    u = [ [0]*n for i in range(n) ]
    for i in range(n):
        u[i][i] = 1
    u[mi][mi] = round(math.cos(fi), 3)
    u[mj][mj] = round(math.cos(fi), 3)
    u[mi][mj] = round(-math.sin(fi), 3)
    u[mj][mi] = round(math.sin(fi), 3)
    return u
def newmatr(aa, uu):
    new = proizv(trans(uu), aa)
    new1 = proizv(new, uu)
    return new1
def pogr(aa):
    p = 0
    for i in range(n):
        for j in range(i):
            p += aa[i][j] * aa[i][j]
    po = math.sqrt(p)
    return round(po, 3)
def skpr(v1, v2):
    sp = 0
    for i in range(n):
        sp += v1[i]*v2[i]
    return sp

sv = []
iter= 0
while True:
    ii = maxnotdiag(a)[1]
    jj = maxnotdiag(a)[2]
    myu=matrvr(ii, jj, a)
    newa = newmatr(a, myu)
    myp = pogr(newa)
    a = newa
    sv.append(myu)
    iter+=1
    if myp<eps or iter == 7:
        break
svs = [ [0]*n for i in range(n) ]
for i in range(n):
    svs[i][i] = 1
for i in range(len(sv)):
    svs = proizv(svs,sv[i])
svs = trans(svs)

print("sobstv znacheniya")
for i in range(n):
    print(a[i][i])
print("sobstv vector")
for i in range(n):
    print(svs[i])