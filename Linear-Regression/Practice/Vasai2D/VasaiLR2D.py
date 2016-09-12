import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.interactive(False)

raw_data = pd.read_csv("linear.csv") #any dataset will work.
raw_data.head(3)
filtered_data = raw_data[~np.isnan(raw_data["y"])] #removes rows with NaN in them
filtered_data.head(3)
print(filtered_data)
npMatrix = np.matrix(filtered_data)
X, Y = npMatrix[:,0], npMatrix[:,1]
mdl = LinearRegression().fit(X,Y) # either this or the next line
#mdl = LinearRegression().fit(filtered_data[['x']],filtered_data.y)
m = mdl.coef_[0]
b = mdl.intercept_
#print ("formula: y = {0}x + {1}".format(m, b)) # following slope intercept form"
print(mdl.score(X,Y))
plt.scatter(X,Y, color='blue')
plt.plot([0,40],[b,m*40+b],'r')
plt.title('Vasai Median Prices', fontsize = 15)
plt.xlabel('Quarter (0 = 2009-Q1, 40 = 2022-Q2)', fontsize = 15)
plt.ylabel('rs/sq.ft', fontsize = 15)
plt.show()
