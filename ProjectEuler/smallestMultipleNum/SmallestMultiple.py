# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


from time import time as time

start_time = time()

for i in range(20, 1000000000):
    count = 0
    for j in range(1,21):
        if i % j != 0:
            break
        elif i % j == 0:
            count += 1
    if count == 20 : 
        print(i)
        break

finish_time = time()
print(finish_time - start_time)
