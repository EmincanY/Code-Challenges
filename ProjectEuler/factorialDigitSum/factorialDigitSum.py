# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(num):
    if (num < 0) | (type(num) != int):
        raise ValueError(
            "You didin't enter a number which could have factorial")
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def factorialDigitSum(num):
    fact = factorial(num)
    total = 0
    
    for i in range(len(str(fact))):
        total += int(str(fact)[i])

    print(total)

factorialDigitSum(100)