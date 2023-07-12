num = int(input())
seq = [num]
while(num != 1):
    if(num % 2 == 0):
        num = num//2
    else:
        num = (num * 3) + 1
    seq.append(num)
    
for e in seq:
    if(e != 1):
        print(e, end=' ')
    else:
        print(e)