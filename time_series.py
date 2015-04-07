
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u'qtconsole')


# In[41]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



# In[53]:

df=pd.read_csv("E:\Users\Mark\Projects\LoanStats3c.csv\LoanStats3c.csv", skiprows=1, header=0, low_memory=False)


# In[93]:

df['issue_d_format']=pd.to_datetime(df['issue_d'])
dfts=df.set_index('issue_d_format')
year_month_summary=dfts.groupby(lambda x : x.year*100 + x.month).count()
loan_count_summary=year_month_summary['issue_d']
loan_count_summary=loan_count_summary[loan_count_summary!=0]


# In[89]:

plt.plot(loan_count_summary)


# In[94]:

sm.graphics.tsa.plot_acf(loan_count_summary)


# In[95]:

sm.graphics.tsa.plot_pacf(loan_count_summary)

