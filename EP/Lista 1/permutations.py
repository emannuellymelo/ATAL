n = int(input())
seq = set(range(1, n+1))
even = []
odd = []
result = ''

if(n == 1):
    print('1')

elif(n > 3):
    for e in seq:
        if(e % 2 == 0):
            even.append(e)
        else:
            odd.append(e)

    result += str(even[0])

    for i in range(1, len(even)):
        result += ' ' + str(even[i])
    
    result += ' ' + str(odd[0])

    for j in range(1, len(odd)):
        result += ' ' + str(odd[j])

    print(result)

else:
    print('NO SOLUTION')
