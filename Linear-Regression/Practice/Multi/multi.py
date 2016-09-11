import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.interactive(False)

ipdata = pd.read_csv("inp.csv") #any dataset will work.
opdata = pd.read_csv("op.csv")
X = ipdata[:]
print(X)
Y = opdata[:]
print(Y)

mdl = LinearRegression().fit(X,Y) # either this or the next line
#mdl = LinearRegression().fit(filtered_data[['x']],filtered_data.y)
print(mdl.coef_)
#m = mdl.coef_[2]
#b = mdl.intercept_
print ("formula: y = {0}x + {1}".format(m, b)) # following slope intercept form"
#plt.scatter(T,P, color='blue')
#plt.plot([0,40],[b,m*40+b],'r')
#plt.title('Vasai Median Prices', fontsize = 15)
#plt.xlabel('Quarter (0 = 2009-Q1, 40 = 2022-Q2)', fontsize = 15)
#plt.ylabel('rs/sq.ft', fontsize = 15)
#plt.show()
