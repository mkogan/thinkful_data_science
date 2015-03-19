import pandas as pd
import matplotlib.pyplot as plt

loansData=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

loansData[['Interest.Rate']]=loansData[['Interest.Rate']].applymap(lambda x:x.strip('%'))
loansData[['Loan.Length']]=loansData[['Loan.Length']].applymap(lambda x:x.strip(' months'))
loansData[['FICO.Score']]=loansData[['FICO.Range']].applymap(lambda x: x.split('-')[1])

loansData[['Interest.Rate','Loan.Length','FICO.Score']]=loansData[['Interest.Rate','Loan.Length','FICO.Score']].astype(float)


plt.figure()
loansData['FICO.Score'].hist()
plt.show()

plt.figure()
a=pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.show()

import numpy as np
import statsmodels.api as sm

intrate=loansData[['Interest.Rate']]
loanamt=loansData[['Amount.Requested']]
fico=loansData[['FICO.Score']]

y=np.matrix(intrate)#.transpose()  ####instruction said to transpose but then i got an 
x1=np.matrix(fico)#.transpose()    ####uneven number of elements error when running OLS  
x2=np.matrix(loanamt)#.transpose() ####so i left these as columns instead of rows

x=np.column_stack([x1,x2])
X=sm.add_constant(x)
model = sm.OLS(y,X)
f=model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
