def is_valid(e, colection):
    if(e in colection):
        return False
    return True

def permutation(array, size, i):
    if i == size:
        yield "".join(array)
    else:
        created = set()
        for j in range(i, size):
            if is_valid(array[j], created):
                created.add(array[j])
                array[i], array[j] = array[j], array[i]
                yield from permutation(array, size, i + 1)
                array[i], array[j] = array[j], array[i]

s_input = input()
s_input = list(s_input)

perms = list(permutation(s_input, len(s_input), 0))
print(len(perms))
perms = sorted(perms)
for res in perms:
    print(res)