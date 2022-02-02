# reaction tester

import random
from time import time, sleep

print("Welcome to the reaction tester")
print("When the prompt appears hit the enter key ")
print("You will have five tries")


total_time = 0

for attempt in range(5):
    print(f'Get ready for try {attempt + 1}')
    sleep(5 * random.random())
    start = time()
    input("Quick hit the enter key!")
    reaction_time = time() - start
    print(f"That was fast it took you {reaction_time:.3f} seconds to hit enter!")
    total_time += reaction_time

average_time = total_time / 5
print('-' * 30)
print(f"Your average time was {average_time:.3f}")