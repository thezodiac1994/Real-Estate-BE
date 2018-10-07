import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.interactive(False)

ipdata = pd.read_csv("inp75.csv") #any dataset will work.
opdata = pd.read_csv("op75.csv")
X = ipdata[:]
Y = opdata[:]

mdl = LinearRegression().fit(X,Y) # either this or the next line
#mdl = LinearRegression().fit(filtered_data[['x']],filtered_data.y)
#print(mdl.coef_)
m = mdl.coef_
c = mdl.intercept_

print(m)
print(c)

#print ("\nPrice = ({})T + ({})D1 + ({})D2 + {}".format(m[0][0],m[0][1],m[0][2],c[0]))
#print("\nT = time,\nD1 = distance from Altamount Road,\nD2 = Distance from Airport")


tipdata = pd.read_csv("tinp25.csv") #any dataset will work.
topdata = pd.read_csv("top25.csv")
tX = tipdata[:]
tY = topdata[:]

hypothesis = np.dot(tX,np.transpose(m)) + c
loss = hypothesis - tY
cost = np.sum(loss ** 2) / (2 * tY.size)


print('Absolute Error')
pd.set_option('display.precision',5)
print(cost)



tYY = tY.values
hy = hypothesis
dtot = 0
tot = 0
mae_num = 0
mae_den = 0
mape = 0


for i in range(0, 1026):

    cu = 0
    if(tYY[i][0]>hy[i][0]):
        cu = (tYY[i][0] - hy[i][0])
    else:
        cu = -(tYY[i][0] - hy[i][0])
    mae_num = mae_num + cu
    mae_den = mae_den + tYY[i][0]
    mape = mape + 100*cu/tYY[i][0]

    #if (i<30):
    #    print(tYY[i][0])
     #   print(hy[i][0])
    #    print("\n")
    tot = tot + cu*cu
    dtot = dtot  + tYY[i][0]*tYY[i][0]
print(tot/dtot)
print(mae_num/mae_den)
print(mape/1026)
