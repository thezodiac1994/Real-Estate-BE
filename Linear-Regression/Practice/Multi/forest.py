import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
plt.interactive(False)

ipdata = pd.read_csv("inp75.csv") #any dataset will work.
opdata = pd.read_csv("op75.csv")
X = ipdata[:]
Y = opdata[:]

mdl = RandomForestRegressor().fit(X,Y) # either this or the next line
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

print(mdl.score(tX,tY))
print(mdl.score(X,Y))


ipdata2 = pd.read_csv("traininp2.csv") #any dataset will work.
opdata2 = pd.read_csv("trainop2.csv")
X2 = ipdata2[:]
Y2 = opdata2[:]

tipdata2 = pd.read_csv("testinp2.csv") #any dataset will work.
topdata2 = pd.read_csv("testop2.csv")
tX2 = tipdata2[:]
tY2 = topdata2[:]


mdl2 = RandomForestRegressor().fit(X2,Y2);

print(mdl2.score(tX2,tY2))
print(mdl2.score(X2,Y2))
print(mdl.score(tX2,tY2))

#plt.scatter(T,P, color='blue')
#plt.plot([0,40],[b,m*40+b],'r')
#plt.title('Vasai Median Prices', fontsize = 15)
#plt.xlabel('Quarter (0 = 2009-Q1, 40 = 2022-Q2)', fontsize = 15)
#plt.ylabel('rs/sq.ft', fontsize = 15)
#plt.show()
