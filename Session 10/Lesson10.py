import numpy as np
import matplotlib.pyplot as plt


def chon_diem(t, m, g, h):
    p1 = []
    z1 = []
    p2 = []
    z2 = []
    for a in range(2):
        for b in range(50):
            c = (int(g[a][b]) - t[0]) ** 2 + (int(h[a][b]) - t[1]) ** 2
            d = (int(g[a][b]) - m[0]) ** 2 + (int(h[a][b]) - m[1]) ** 2
            if c <= d:
                p1.append(c)
                z1.append([g[a][b], h[a][b]])
            else:
                p2.append(d)
                z2.append([g[a][b], h[a][b]])
    return [z1, z2]


def tam_moi(r):
    tong_x1 = 0
    tong_y1 = 0
    tong_x2 = 0
    tong_y2 = 0
    for j in range(len(r[0])):
        tong_x1 += int(r[0][j][0])
        tong_y1 += int(r[0][j][1])
    for k in range(len(r[1])):
        tong_x2 += int(r[1][k][0])
        tong_y2 += int(r[1][k][1])
    new_center1 = (tong_x1 / 50, tong_y1 / 50)
    new_center2 = (tong_x2 / 50, tong_y2 / 50)
    return [new_center1, new_center2]


#
x1 = np.random.randint(0, 50, size=50)
x2 = np.random.randint(50, 100, size=50)
x = [x1, x2]
y1 = np.random.randint(0, 50, size=50)
y2 = np.random.randint(50, 100, size=50)
y = [y1, y2]
k1 = [np.random.randint(0, 100), np.random.randint(0, 100)]
k2 = [np.random.randint(0, 100), np.random.randint(0, 100)]
z0 = chon_diem(k1, k2, x, y)
x0 = []
y0 = []
for o in range(30):
    tam = tam_moi(z0)
    if (tam[0][0] - k1[0])**2 + (tam[0][1] - k1[1])**2 < 1 and (tam[1][0] - k2[0])**2 + (tam[1][1] - k2[1])**2 < 1:
        x0.append(tam[0][0])
        x0.append(tam[1][0])
        y0.append(tam[0][1])
        y0.append(tam[1][1])
        break
    else:
        k1 = [tam[0][0], tam[0][1]]
        k2 = [tam[1][0], tam[1][1]]
        z0 = chon_diem(k1, k2, x, y)
print(x0)
print(y0)
plt.scatter(x, y, color='r')
plt.scatter(x0, y0, color='b')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
