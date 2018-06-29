import numpy as np
np.random.seed(6)
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
# make_blobs()
[x,y] = make_blobs(50,2,2,1.05,random_state = 40, shuffle= True)
print(x)
print(y)

plt.scatter(x[:,0],x[:,1],marker='o',c=y)
plt.axis([-5,10,-12,-1])
plt.show()

positive = []
negative = []

for i,v in enumerate(y):
    if v==0:
        negative.append(x[i])
    elif v==1:
        positive.append(x[i])

#tao 1 tu dien du lieu

data_dict = {-1:np.array(negative),1:np.array(positive)}
print((data_dict))

w = []
b = []
max_value = float('+inf')
min_value = float('-inf')
for i in data_dict:
    if np.amax(data_dict[i])> max_value:
        max_value = np.amax(data_dict[i])
    if np.amin(data_dict[i])< min_value:
        min_value = np.min(data_dict[i])

print(max_value)
print(min_value)

w = []
b = []
learning_rate = [max_value*0.1, max_value*0.01, max_value*0.001]

w = []
b = []

def svm_new(data_dict):
    global w
    global b

    factor = 0.5*max_value

    # for lrate in learning_rate: