import sys

index = int(sys.argv[1])
fileName = sys.argv[2]

numList = []

with open(fileName, 'r') as file:
    for i in file:
        numStr = i.strip().split()[index]
        numList.append(float(numStr))

numList.sort()
print(','.join([str(i) for i in numList]))
