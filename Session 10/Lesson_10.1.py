import numpy as np
import matplotlib.pyplot as plt
#
x1 = np.random.randint(0,50,size = 50)
x2 = np.random.randint(50,100,size = 50)
x = [x1,x2]
y1 = np.random.randint(0,50,size = 50)
y2 = np.random.randint(50,100,size = 50)
y = [y1,y2]

#Khoi tao k tam cluster
c1 = [30,30]
c2 = [70,70]
a=[]
for i in x1:
    a.append(i)
for i in x2:
    a.append(i)

b=[]
for i in y1:
    b.append(i)
for i in y2:
    b.append(i)
cluster1x = []
cluster1y = []
cluster2x = []
cluster2y = []
epsilon = 1
old_cluster1 = c1
old_cluster2 = c2
n_current = 100
for n in range(n_current):
    #tinh toan khoang cach tu moi diem du lieu toi tam
    for i in range(100):
        d1 = (a[i]-c1[0])**2 + (b[i]-c1[1])**2
        d2 = (a[i]-c2[0]) ** 2 + (b[i]-c2[1]) ** 2
    #gan du lieu toi cluster phu hop dua vao khoang cach
        if d1<d2:
            cluster1x.append(a[i])
            cluster1y.append(b[i])
        else:
            cluster2x.append(a[i])
            cluster2y.append(b[i])
#tinh lai tam moi cho cluster (tim mean cua cac diem = sum/len)
    sum1x = 0
    for j in range(len(cluster1x)):
        sum1x = cluster1x[j] + sum1x
        c1[0] = sum1x/len(cluster1x)
    sum1y = 0
    for j in range(len(cluster1y)):
        sum1y = cluster1y[j] + sum1y
        c1[1] = sum1y/len(cluster1y)
    sum2x = 0
    for j in range(len(cluster2x)):
        sum2x = cluster2x[j] + sum2x
        c2[0] = sum2x/len(cluster2x)
    sum2y = 0
    for j in range(len(cluster2y)):
        sum2y = cluster2y[j] + sum2y
        c2[1] = sum2y/len(cluster2y)
#tinh khoang cach tam moi den tam cu
    s1 = (c1[0]-old_cluster1[0])**2 + (c1[1]-old_cluster1[1])**2
    s2 = (c2[0]-old_cluster2[0])**2 + (c2[1]-old_cluster2[1])**2
    if s1 < epsilon and s2 < epsilon:
        break

plt.scatter(x,y,color = 'r')
plt.scatter(c1[0],c1[1],color = "g")
plt.scatter(c2[0],c2[1],color = "g")
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()