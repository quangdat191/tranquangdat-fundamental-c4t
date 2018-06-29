import numpy as np
import matplotlib.pyplot as plt
#
x1 = np.random.randint(0,50,size = 50)
x2 = np.random.randint(50,100,size = 50)
x = [x1,x2]
y1 = np.random.randint(0,50,size = 50)
y2 = np.random.randint(50,100,size = 50)
y = [y1,y2]

# k1 = [np.random.randint(0,100),np.random.randint(0,100)]
# k2 = [np.random.randint(0,100),np.random.randint(0,100)]
# for i in range(100):
#     d**2 = (k1-x1)**2 + (k2-y2)**2

plt.scatter(x,y,color = 'r')
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()

def phan_cum (x,y,centrod1,centrod2):
    cluster1 = [], cluster2 = []
    for i in range(100):
        d1 = (x1-centrod1)**2 + (y1-centrod2)**2
        d2 = (x2-centrod1)**2 + (y2-centrod2)**2
        if d1 < d2:
            cluster1.append([x[i],y[i]])
        else:
            cluster2.append([x[i],y[i]])
    cluster = []
    cluster.append(cluster1)
    cluster.append(cluster2)
    return cluster

def Mean(cluster):
    xmean = 0
    ymean = 0
    for i in range(len(cluster)):
        xmean = cluster[i][0] + xmean
        ymean = cluster[i][1] + ymean
    xmean = xmean/len(cluster)
    ymean = ymean/len(cluster)
    return xmean,ymean

e = 1
n_current = 100
cluster1 = []
cluster2 = []
for n in range(n_current):
    old_centrod1 = (30,30)
    old_centrod2 = (70,70)
    phan_cum(x,y,old_centrod1,old_centrod2)
    centrod1 = Mean(cluster1)
    centrod2 = Mean(cluster2)
    x1,y1 = old_centrod1[0][0],old_centrod1[0][1]
    x2,y2 = old_centrod2[0][0],old_centrod2[0][1]
    d1 = (x1-centrod1[0][0])**2+(y1-centrod1[0][1])**2
    d2 = (x2-centrod2[0][0])**2+(y2-centrod2[0][1])**2
    if d1 < e and d2 <e:
        break



