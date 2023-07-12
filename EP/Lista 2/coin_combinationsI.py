qtd_moedas, troco = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
modulo = 1000000007
stg = [0] * (troco + 1)
stg[0] = 1
i = 1
while(i <= troco):
    m = 0
    while(m < qtd_moedas):
        rest = i - (c[m])
        if rest >= 0:
            stg[i] += stg[rest]
            stg[i] %= modulo
        m += 1
    i += 1
    
print(stg[troco]%modulo)
