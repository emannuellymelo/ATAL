def turn_int(array):
    new = []
    for e in array:
        new.append(int(e))
    return new
    
while True:
    n = int(input())
    if n == 0:
        break
    new = input().split(" ")
    new = turn_int(new)
    work = 0
    soma = 0
    for i in range(len(new)):
        soma+= int(new[i])
        work+= abs(soma)
    print(work)
    