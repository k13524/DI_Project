import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter

df2013_2014 = pd.read_sas('DR1IFF_G.XPT')
df2014_2015 = pd.read_sas('DR1IFF_H.XPT')
df2015_2016 = pd.read_sas('DR1IFF_I.XPT')

#Drop of uninterested columns
df2013_2014 = df2013_2014.drop(['WTDRD1', 'WTDR2D', 'DR1DRSTZ', 'DR1EXMER', 'DRDINT', 'DR1DBIH', 'DR1_020', 'DR1IFDCD'], axis=1)
df2014_2015 = df2014_2015.drop(['WTDRD1', 'WTDR2D', 'DR1DRSTZ', 'DR1EXMER', 'DRDINT', 'DR1DBIH', 'DR1_020', 'DR1IFDCD'], axis=1)
df2015_2016 = df2015_2016.drop(['WTDRD1', 'WTDR2D', 'DR1DRSTZ', 'DR1EXMER', 'DRDINT', 'DR1DBIH', 'DR1_020', 'DR1IFDCD'], axis=1)

#Filter the data by only looking at the non breast-fed infants
df2013_2014 = df2013_2014.query('DRABF == 2')
df2014_2015 = df2014_2015.query('DRABF == 2')
df2015_2016 = df2015_2016.query('DRABF == 2')
'''
df_concat = pd.concat([df2013_2014[['DR1LANG','DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']],\
 df2014_2015[['DR1LANG','DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']], \
 df2015_2016[['DR1LANG','DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']]], axis=0)
datatest = df_concat[['DR1LANG','DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']]
co = datatest.corr(method='pearson')
sns.heatmap(co)
plt.show()
'''


#Breakfast 
df2013_2014_breakfast = df2013_2014.query('DR1_030Z == 1')
df2014_2015_breakfast = df2014_2015.query('DR1_030Z == 1')
df2015_2016_breakfast = df2015_2016.query('DR1_030Z == 1')

#Lunch
df2013_2014_lunch = df2013_2014.query('DR1_030Z == 2')
df2014_2015_lunch = df2014_2015.query('DR1_030Z == 2')
df2015_2016_lunch = df2015_2016.query('DR1_030Z == 2')

#Dinner
df2013_2014_dinner = df2013_2014.query('DR1_030Z == 3')
df2014_2015_dinner = df2014_2015.query('DR1_030Z == 3')
df2015_2016_dinner = df2015_2016.query('DR1_030Z == 3')

print(df2013_2014_dinner.query('DR1IPROT <10'))
'''
indexNames = df2013_2014[ df2013_2014['DR1IPROT'] > 100 ].index
# Delete these row indexes from dataFrame
df2013_2014.drop(indexNames , inplace=True)

dfbox = pd.DataFrame(df2013_2014[['DR1IPROT','DR1ICARB']], columns=['DR1IPROT','DR1ICARB'])
axes = dfbox.plot.box()
axes.set_ylim([0,100])
plt.show()


print(df2013_2014_breakfast[['DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']].mean(),\
df2013_2014_breakfast[['DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']].std())
print(df2014_2015_breakfast[['DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']].mean())
print(df2015_2016_breakfast[['DR1IPROT','DR1ICARB','DR1IFIBE','DR1ICALC','DR1IMAGN','DR1IIRON','DR1IVARA','DR1IVD','DR1IVC']].mean())
'''















