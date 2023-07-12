seq = input()
counts = [0, 0, 0, 0]
countsMax = 0
lastIndex = 0

for e in seq:
    if(e == 'A'):
        if(lastIndex != 0):
            counts[0] = 0
        lastIndex = 0

    elif(e == 'C'):
        if(lastIndex != 1):
            counts[1] = 0
        lastIndex = 1

    elif(e == 'G'):
        if(lastIndex != 2):
            counts[2] = 0
        lastIndex = 2

    elif(e == 'T'):
        if(lastIndex != 3):
            counts[3] = 0
        lastIndex = 3

    counts[lastIndex] += 1
    if(countsMax < counts[lastIndex]):
        countsMax = counts[lastIndex]

print(countsMax)