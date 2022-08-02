def isPrime(num):
    from math import sqrt as sq
    if num < 2 or type(num) == float:
        return False
    else:
        for i in range(2, int(sq(num)+1)):
            if num % i == 0:
                return False
        return True


primeList = []
for i in range(1000000):
    if isPrime(i):
        primeList.append(i)
print(primeList)

max_difference = 0
for i in range(len(primeList)-1):
    if primeList[i+1]-primeList[i] > max_difference:
        max_difference = primeList[i+1]-primeList[i]


print(max_difference)
