import numpy as np
import matplotlib.pyplot as plt



#
a=[]
b=[]
x1 = np.random.randint(0,50,size = 50)
x2 = np.random.randint(50,100,size = 50)
x = [x1,x2]
for i in x1:
    a.append(i)
for i in x2:
    a.append(i)
y1 = np.random.randint(0,50,size = 50)
y2 = np.random.randint(50,100,size = 50)
y = [y1,y2]
for i in y1:
    b.append(i)
for i in y2:
    b.append(i)
c1 = [30,30]
c2 = [70,70]
epsilon =1
while True:
    c1old = c1
    c2old = c2
    cluster1x = []
    cluster1y = []
    cluster2x = []
    cluster2y = []
    sum = 0
    for i in range(100):
        d1 = (a[i] - c1[0])**2 + (b[i] - c1[1])**2
        d2 = (a[i] - c2[0])**2 + (b[i] - c2[1])**2
        if d1<d2:
            cluster1x.append(a[i])
            cluster1y.append(b[i])
        else:
            cluster2x.append(a[i])
            cluster2y.append(b[i])
    for i in range(len(cluster1x)):
        sum += cluster1x[i]
        c1[0] = sum / len(cluster1x)
    sum = 0
    for i in range(len(cluster1y)):
        sum += cluster1x[i]
        c1[1] = sum / len(cluster1y)
    sum = 0
    for i in range(len(cluster2x)):
        sum += cluster2x[i]
        c2[0] = sum / len(cluster2x)
    sum = 0
    for i in range(len(cluster2y)):
        sum += cluster2x[i]
        c2[1] = sum / len(cluster2y)
    sum = 0
    if (c1old[0]-c1[0])**2 + (c1old[1]-c1[1])**2 < epsilon**2 and (c2old[0] - c2[0]) ** 2 + (c2old[1] - c2[1]) ** 2 < epsilon ** 2:
        break


plt.scatter(c1[0],c1[1],color='g')
plt.scatter(c2[0],c2[1],color='g')
plt.scatter(x,y,color = 'r')
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()
