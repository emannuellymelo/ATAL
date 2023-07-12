def count_dice_combination(n):
    modulo = 1000000007
    stg = [0] * (n+1)
    stg[0], stg[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, 7):
            if i >= j:
                stg[i] += (stg[i-j])%modulo
            else: break
    return stg[-1]%modulo
    
n = int(input())
print(count_dice_combination(n))
