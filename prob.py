import collections
import scipy.stats as stats
import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)

print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

plt.hist(x, histtype='bar')
plt.savefig('E:\Users\Mark\Documents\Python Scripts\\histplot.png')
plt.figure()
plt.boxplot(x)
plt.savefig('E:\Users\Mark\Documents\Python Scripts\\boxplot.png')
plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.show()