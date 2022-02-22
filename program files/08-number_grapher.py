import matplotlib.pyplot as plt
import os
import random

# generate random numbers and write to file
file = open("integers.txt", "w")

for number in range(1, 501):
    file.write(str(random.randint(number, 501)) + "\n")
file.close()


# read file and graph data

file = open("integers.txt", "r")

raw = file.readlines()
file.close()
data = []
for point in raw:
    data.append(int(point.strip()))


# print(os.getcwd())
print(data)


plt.plot(data)
plt.show()



















