X=[-1, 0, 1, 2, 3]
Y=[-0.7854, 0, 0.7854, 1.1071, 1.249]
x=1

n=len(X)
for i in range(n):
    if x>X[i] and x<=X[i+1]:
        s1=(Y[i+1]-Y[i])/(X[i+1]-X[i])
        s2=(Y[i+2]-Y[i+1])/(X[i+2]-X[i+1])
        y1=s1+(s2-s1)/(X[i+2]-X[i])*(2*x-X[i]-X[i+1])
        y2=2*(s2-s1)/(X[i+2]-X[i])
print(s1)
print(s2)
print("y'(",x,") =",y1)
print("y''(",x,") =", y2)