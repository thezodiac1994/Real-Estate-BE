import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
plt.interactive(False)
'''
def distance (data1,data2) :
    dist = 0
    for i in range (0,6): # params
        dist = dist + (data1[i] -  data2[i])*(data1[i] - data2[i])
    return sqrt (dist)

def _predict (data) :
    vector < pair  <int,int>> dist  # distance and index
    for i in range(0,1026)
        dist[i].first = distance (mdl[i],data)
        dist[i].second = i

    sort (dist.begin(), dist.end())
    ans = 0

    for i in range (0,mdl.k)
        ans = ans + mdl.value(dist[i].second)

    return ans/mdl.k
'''

ipdata = pd.read_csv("inp75.csv") #any dataset will work.
opdata = pd.read_csv("op75.csv")
X = ipdata[:]
Y = opdata[:]

mdl = KNeighborsRegressor(7)
mdl.fit(X,Y) # either this or the next line
#mdl = LinearRegression().fit(filtered_data[['x']],filtered_data.y)
#print(mdl.coef_)
#m = mdl.coef_
#c = mdl.intercept_
#print ("\nPrice = ({})T + ({})D1 + ({})D2 + {}".format(m[0][0],m[0][1],m[0][2],c[0]))
#print("\nT = time,\nD1 = distance from Altamount Road,\nD2 = Distance from Airport")


tipdata = pd.read_csv("tinp25.csv") #any dataset will work.
topdata = pd.read_csv("top25.csv")
tX = tipdata[:]
tY = topdata[:]



#print(mdl.score(tX,tY))
#print(mdl.score(X,Y))


#ipdata2 = pd.read_csv("traininp2.csv") #any dataset will work.
#opdata2 = pd.read_csv("trainop2.csv")
#X2 = ipdata2[:]ol
#Y2 = opdata2[:]

#tipdata2 = pd.read_csv("testinp2.csv") #any dataset will work.
#topdata2 = pd.read_csv("testop2.csv")
#tX2 = tipdata2[:]
#tY2 = topdata2[:]


#mdl2 = KNeighborsRegressor(5);
#mdl2.fit(X2,Y2);

#print(mdl2.score(tX2,tY2))
#print(mdl2.score(X2,Y2))
#print(mdl.score(tX2,tY2))

#plt.scatter(T,P, color='blue')
#plt.plot([0,40],[b,m*40+b],'r')
#plt.title('Vasai Median Prices', fontsize = 15)
#plt.xlabel('Quarter (0 = 2009-Q1, 40 = 2022-Q2)', fontsize = 15)
#plt.ylabel('rs/sq.ft', fontsize = 15)
#plt.show()


tYY = tY.values
hy = mdl.predict(tX)
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
    mape = mape + 100*cu/(1026*tYY[i][0])

    #if (i<30):
    #    print(tYY[i][0])
     #   print(hy[i][0])
    #    print("\n")
    tot = tot + cu*cu
    dtot = dtot  + tYY[i][0]*tYY[i][0]
print(tot/dtot)
print(mae_num/mae_den)
print(mape)



tipdata = pd.read_csv("vasai_test.csv") #any dataset will work.
tX = tipdata[:]
tY = mdl.predict(tX)

print(tY)