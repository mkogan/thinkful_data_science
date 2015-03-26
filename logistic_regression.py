
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import math as mt

loansData=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

loansData[['Interest.Rate']]=loansData[['Interest.Rate']].applymap(lambda x:x.strip('%'))
loansData[['Loan.Length']]=loansData[['Loan.Length']].applymap(lambda x:x.strip(' months'))
loansData[['FICO.Score']]=loansData[['FICO.Range']].applymap(lambda x: x.split('-')[1])

loansData[['Interest.Rate','Loan.Length','FICO.Score']]=loansData[['Interest.Rate','Loan.Length','FICO.Score']].astype(float)

loansData['IntRate12']=loansData['Interest.Rate']<12

loansData['Int1']=1

ind_vars=['Amount.Funded.By.Investors','FICO.Score','Int1']



# In[10]:

logit = sm.Logit(loansData['IntRate12'], loansData[ind_vars])
result=logit.fit()
coeff=result.params


# In[11]:

print coeff


def logistic_function(coeff, loan, fico):
    pX=1-1/(1+mt.exp(coeff[2]+coeff[0]*loan+coeff[1]*fico))
    return pX


# In[14]:

print logistic_function(coeff, 10000, 720), ' since p < 0.70 we will not get the loan'


# In[28]:

x=range(600,800)
y=[logistic_function(coeff,10000,i) for i in x]

loansData[['logit70']]=loansData[['FICO.Score']].applymap(lambda x:logistic_function(coeff,10000,x)>0.7)


# In[45]:

plt.plot(x,y,'b-')

x1=loansData['FICO.Score'][loansData['Amount.Funded.By.Investors']==10000]
y1=loansData['logit70'][loansData['Amount.Funded.By.Investors']==10000]

plt.plot(x1,y1, 'ro')
plt.show()