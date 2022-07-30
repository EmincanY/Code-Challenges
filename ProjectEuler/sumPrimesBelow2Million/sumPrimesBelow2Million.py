def isPrime(num):
    from math import sqrt as sqrt
    if num < 2 or type(num) == float:
        return False
    else:
        for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

total = 0
for i in range(1,2000001):
    if isPrime(i):
        total += i
        
print(total)