
fiboList = [1, 1]

for i in range(10000):
    newNum = fiboList[i] + fiboList[i+1]
    fiboList.append(newNum)
    if len(str(newNum)) == 1000:
        index1000digit = fiboList.index(newNum)
        print(f"First 1000digit fibonacci number is {index1000digit+1}st fibonacci number.")
        break
