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
for i in range(225):
    if isPrime(i):
        primeList.append(i)


for x in range(220):
    if primeList[x]+primeList[x+1]+primeList[x+2]+primeList[x+3] == 220:
        print(primeList[x], primeList[x+1], primeList[x+2], primeList[x+3])
        break
