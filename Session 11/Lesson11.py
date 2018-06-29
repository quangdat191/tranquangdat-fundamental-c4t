import numpy as np
import random
import matplotlib.pyplot as plt


def mul_matrix(a, b):
    result = []
    if len(a) == len(b[0]):
        for m in range(len(a[0])):
            d = []
            for n in range(len(b)):
                c = 0
                for p in range(len(a)):
                    c += a[p][m] * b[n][p]
                d.append(c)
            result.append(d)
        return result
    else:
        print("Dimension error")


def hard_lim(value):
    if value >= 0:
        return 1
    else:
        return 0


x1 = np.random.randint(0, 50, size=50)
y1 = np.random.randint(0, 50, size=50)
P1 = []
t1 = []
x10 = 0
y10 = 0
for i in range(50):
    x10 += x1[i]
    y10 += y1[i]
    P1.append((x1[i], y1[i]))
    t1.append(0)
x10 /= 50
y10 /= 50
print(P1)
# print(t1)
x2 = np.random.randint(50, 100, size=50)
y2 = np.random.randint(50, 100, size=50)
P2 = []
t2 = []
x20 = 0
y20 = 0
for i in range(50):
    x20 += x2[i]
    y20 += y2[i]
    P2.append((x2[i], y2[i]))
    t2.append(1)
x20 /= 50
y20 /= 50
print(P2)
# print(t2)
w = [[0], [0]]
b0 = 0
count = 0
while not count == 100:
    count = 0
    for i in range(100):
        if i < 50:
            Pi = [P1[i]]
            ti = t1[i]
        else:
            Pi = [P2[i - 50]]
            ti = t2[i - 50]
        val = mul_matrix(w, Pi)[0][0] + b0
        ret = hard_lim(val)
        if ret == ti:
            count += 1
        else:
            e = ti - ret
            Pi_transposed = []
            for j in Pi:
                for k in j:
                    Pi_transposed.append([k])
            w_new = []
            for h in range(len(w)):
                w_new.append([w[h][0] + e * Pi_transposed[h][0]])
            b0 = b0 + e
            w = w_new
print(w)
print(b0)
x0 = np.linspace(0, 100)
y0 = -(w[0][0] * x0 + b0) / w[1][0]
y00 = -((x20 - x10) * x0 - (x20 - x10) * (x20 + x10) / 2 - (y20 - y10) * (y20 + y10) / 2) / (y20 - y10)
y000 = 100 - x0
plt.plot(x0, y0, color='b')
plt.plot(x0, y00, color='r')
plt.plot(x0, y000, color='g')
plt.scatter(x1, y1, color='r')
plt.scatter(x2, y2, color='g')
plt.scatter(x10, y10, color='g')
plt.scatter(x20, y20, color='r')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()
