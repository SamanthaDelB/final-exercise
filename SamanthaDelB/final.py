import sys
import numpy as np
import matplotlib.pyplot

data = np.loadtxt(fname = '../gapminder_gdp_americas.csv', delimiter = ',', skiprows=(1), usecols=(1,2,3,4,5,6,7,8,9,10,11,12))

#print data
print data.shape

data_mean = data.mean(axis=0)
print data_mean
print data_mean.shape

dates = ['1952', '1957', '1962', '1967', '1972', '1977', '1982', '1987', '1992', '1997', '2002', '2007']

fig = matplotlib.pyplot.figure(figsize=(20.0,8.0))

axis = fig.add_subplot(1,1,1)
#axis.bar(dates, data_mean, width=2)
axis.bar(range(len(dates)), data_mean, width=0.75)
axis.set_xticks(np.arange(len(dates)) + 0.35)
axis.set_ylabel('average GDP per capita per year')
axis.set_xlabel('Year')
axis.set_xticklabels(dates, rotation=90)

matplotlib.pyplot.savefig('final.png')
matplotlib.pyplot.show()