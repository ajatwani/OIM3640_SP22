import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from time import sleep, time

# data = pdr.get_data_yahoo('GOOG', start = '2021-03-09')
# print(data)
# print(type(data))
# print(data.info())
# plt.plot(data['Close'])
# plt.show()
start_time = time()
while True:
    print(pdr.get_quote_yahoo('GOOG')['price'])
    sleep(1)
    if time() - start_time >= 5:
        prompt = input("Press enter to continue: ")
        start_time = time()
        if prompt.isalpha():
            break





