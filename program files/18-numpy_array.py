import matplotlib.pyplot as plt
import numpy as np

file = open('gbtc.csv', 'r')

header = file.readline()
data = file.readlines()
array = np.zeros(len(data))
prices = []
for line in data:
    line = line.split(',')
    prices.append(float(line[1].strip()))
prices =np.array(prices)
# plt.plot(prices)
# plt.show()

pct_change = [ e/b -1 for e,b in zip(prices[1:], prices)]
plt.hist(pct_change, bins = 50, edgecolor='w')
plt.show()
# print(prices)
# print(header)
# print(prices)
   