import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

lend_club=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
lend_club.dropna(inplace=True)

freq=collections.Counter(lend_club['Open.CREDIT.Lines'])

chi, p = stats.chisquare(freq.values())

print chi, p
