# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromeNum(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

eligiblePalindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindromeNum(i*j):
            eligiblePalindromes.append(i*j)

eligiblePalindromes = sorted(eligiblePalindromes, reverse=False)
print(eligiblePalindromes[-1])
