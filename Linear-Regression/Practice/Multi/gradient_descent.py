import numpy as np
import pandas as pd

def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x,theta)
        #print(hypothesis.shape)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        #print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta

ipdata = pd.read_csv("ginp75.csv") #any dataset will work.
opdata = pd.read_csv("op75.csv")
X = ipdata[:]
Y = opdata[:]

row,col =  (X.shape)
#theta = np.zeros((col,row))
theta = pd.DataFrame(np.zeros((col,1)))
#print(theta.shape)
#theta =  zeros(Y.size)
#theta = transpose(theta)

#XX = dict.items()
#print(type(X))
#print(Y.size)
theta1 = gradientDescent(X,Y,theta,0.0001,Y.size,1000) #
print(theta1)
#
tipdata = pd.read_csv("gtinp25.csv") #any dataset will work.
topdata = pd.read_csv("top25.csv")
tX = tipdata[:]
tY = topdata[:]

hypothesis = np.dot(tX, theta1)
loss = hypothesis - tY
cost = np.sum(loss ** 2) / (2 * tY.size)

pd.set_option('display.precision',5)
print(cost)

tot = 0
print(tY.shape)
print(len(tY))

tYY = tY.values
hy = hypothesis

for i in (0, 1025):
    cu = 0
    if(tYY[i][0]>hy[i][0]):
        cu = (tYY[i][0] - hy[i][0])
    else:
        cu = -(tYY[i][0] - hy[i][0])
    cu = cu/tYY[i][0]
    tot = tot + cu

print(100 - 100 * tot/1025)
#print(mdl.score(tX,tY))
#print(mdl.score(X,Y))
