from cmath import sqrt
import math
print("kolvo strok")
n = int(input())
print("matrix")
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print("epsilon")
eps=float(input())

def trans(m):
    res = [[m[j][i] for j in range(n)] for i in range(n)]
    return res
def proizv(m1, m2):
    res = [ [0]*n for i in range(n) ]
    for i in range(n):
        for j in range(n):       
            res[i][j] = round(sum(m1[i][k] * m2[k][j] for k in range(n)), 3)
    return res
def sgn(a):
    if a<0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1
def pogr(m):
    p=0
    for i in range(1, n):
        for j in range(i):
            p += m[i][j] ** 2
    po = math.sqrt(p)
    return po
def sumfor(m, jj):
    res = 0 
    for i in range(jj, n):
        res += m[i][jj] ** 2
    return res
def matrch(m, ch):
    res = [ [0]*n for i in range(n) ] 
    for i in range(n):
        for j in range(n):
            res[i][j] = round(m[i][j] * ch, 3)
    return res
def summat(m1, m2):
    res = [ [0]*n for i in range(n) ] 
    for i in range(n):
        for j in range(n):
            res[i][j] = round(m1[i][j] + m2[i][j], 3)
    return res
def findhd(v):
    me = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    hh = [ [0]*n for i in range(n) ] 
    for i in range(n):
        for j in range(n):
            hh[i][j] = v[i]*v[j]
    delit = 0
    for i in range(n):
        delit += v[i] ** 2
    hh = matrch(hh, -2/delit)
    h = summat(me, hh)
    return h
def triug(m):
    s = 0
    for i in range(n):
        for j in range(i):
            s += abs(m[i][j])
    if s < 0.1:
        return 1
    else:
        return 0
def qr(a):
    ao = a
    q = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    v = [ [0]*n for i in range(n) ] 
    for i in range(n-1):
        for j in range(n):
            if i>j:
                v[i][j] = 0
            elif i == j:
                v[i][j] = round(ao[i][j] + sgn(ao[i][j])*math.sqrt(sumfor(ao, i)), 3)
            else:
                v[i][j] = ao[j][i]
        h = findhd(v[i])
        q = proizv(q, h)
        ao=proizv(h, ao)
    return q, ao
    
an = a
iter = 0
while True:
    qn, rn = qr(an)
    for i in range(n):
        for j in range(i):
            rn[i][j] = 0
    an = proizv(rn, qn)
    iter+=1
    if pogr(an) < eps:
        break
print("sobstv znach:")
for i in range(n):
    print(an[i][i])
