# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 21:22:51 2015

@author: Mark
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

#plt.plot(range(15),'o') 

df=pd.read_csv("E:\Users\Mark\Projects\LoanStats3c.csv\LoanStats3c.csv", 
               skiprows=1, header=0, index_col=0)

df=df.dropna()               

df['int_rate2']=df[['int_rate']].applymap(lambda x: float(str(x).strip('%')))
               
X=np.log1p(df[['annual_inc']])
y=df.int_rate2

X=sm.add_constant(X)

est=sm.OLS(y,X).fit()

est.summary()

plt.scatter(X.annual_inc,y, alpha=0.3)
plt.xlabel("Log income")
plt.ylabel("interest rate")
inspace=np.linspace(X.annual_inc.min(),X.annual_inc.max(),100)
plt.plot(inspace, est.params[0]+est.params[1]*inspace)


df['home_own_ord']=pd.Categorical(df.home_ownership).labels

X['home_own']=df['home_own_ord']

est=sm.OLS(y,X).fit()

est.summary()


plt.scatter(X.annual_inc,y, alpha=0.3)
plt.xlabel("Log income")
plt.ylabel("interest rate")

inspace=np.linspace(X.annual_inc.min(),X.annual_inc.max(),100)

plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*0)
plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*1
    ,'r',label='OWN')
plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*2
    ,'g',label='RENT')
    
plt.legend()    
    
plt.figure()


X['home_income']=X.annual_inc*X.home_own

est=sm.OLS(y,X).fit()

est.summary()

plt.scatter(X.annual_inc,y, alpha=0.3)
plt.xlabel("Log income")
plt.ylabel("interest rate")

inspace=np.linspace(X.annual_inc.min(),X.annual_inc.max(),100)

plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*0
    +est.params[3]*inspace*0, label='MORTGAGE')
plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*1
    +est.params[3]*inspace*1,'r',label='OWN')
plt.plot(inspace, est.params[0]+est.params[1]*inspace+est.params[2]*2
    +est.params[3]*inspace*2,'g',label='RENT')
    
plt.legend()