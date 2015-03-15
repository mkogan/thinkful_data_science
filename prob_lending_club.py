import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

lend_club=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
lend_club.dropna(inplace=True)

lend_club.boxplot(column='Amount.Requested')

#plot box_plot
plt.savefig('E:\Users\Mark\Projects\Thinkful\\2.2.2\\amnt_req_boxplot.png')
plt.figure()

#plot histogram
lend_club.hist(column='Amount.Requested')
plt.savefig('E:\Users\Mark\Projects\Thinkful\\2.2.2\\amnt_req_hist.png')
plt.figure()

#plot qq plot
amnt_requested_qqp=stats.probplot(lend_club['Amount.Requested'],dist='norm',plot=plt)
plt.savefig('E:\Users\Mark\Projects\Thinkful\\2.2.2\\amnt_req_qq.png')
plt.figure()

"""
The median of amounts requested is ~ $10,000, with an inter-quartile range of roughly $11,000. 
The historgram is skewed-right, and from the qq plot we can conclude the data is not normally distributed
because the quartiles do not follow a straight line.
This dataset is very similar to the amount funded by investors in nearly every respect. With the 
exceptions that the amount funded by investors appears to have a narrower iqr.
"""