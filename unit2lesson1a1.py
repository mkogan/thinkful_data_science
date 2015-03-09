# -*- coding: utf-8 -*-
"""
Created on Sun Mar 08 22:11:13 2015

@author: Mark
"""

import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1:]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alMean=df['Alcohol'].mean() 
alMed=df['Alcohol'].median() 
alMode=stats.mode(df['Alcohol']) 


toMean=df['Tobacco'].mean() 
toMed=df['Tobacco'].median() 
toMode=stats.mode(df['Tobacco'])

alRange=max(df['Alcohol']) - min(df['Alcohol'])
alStd=df['Alcohol'].std() 
alVar=df['Alcohol'].var() 

toRange=max(df['Tobacco']) - min(df['Tobacco'])
toStd=df['Tobacco'].std() 
toVar=df['Tobacco'].var() 

print 'The mean, median and mode for weekly alcohol consumption in the UK is {0:.1f}, {1:.1f}, {2:.1f}.'.format(alMean,alMed,float(alMode[0][0]))

print 'And the range, standard deviation and variance is {0:.1f}, {1:.1f}, {2:.1f}.'.format(alRange,alStd,alVar)
    
print 'The mean, median and mode for weekly tobacco consumption in the UK is {0:.2g}, {1:.2g}, {2:.2g}.'.format(toMean, toMed, float(toMode[0]))

print 'And the range, standard deviation and variance is {0:.1f}, {1:.1f}, {2:.1f}.'.format(toRange,toStd,toVar)