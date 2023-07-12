def is_valid(x, new_pot, res):
    new_res = res + new_pot
    if(new_res > x):
        return False
    return True

def find_sum(x, n, c, res, j, combs):
    if(j == len(c)):
        if(res == x):
            combs.append(1)
    else:
        new_pot = c[j] ** n
        aux = False
        if(is_valid(x, new_pot, res)):
            res += new_pot
            aux = True
            find_sum(x, n, c, res, j+1, combs)
        if(aux):
            res -= new_pot
        find_sum(x, n, c, res, j+1, combs)

x = int(input())
n = int(input())

c = list(range(1, int(x**(1/n) + 1)))
res = 0
j = 0
combs = []
find_sum(x, n, c, res, j, combs)
print(len(combs))