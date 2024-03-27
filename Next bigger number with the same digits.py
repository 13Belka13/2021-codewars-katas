from itertools import permutations as p
def next_bigger(n):
    l = list(sorted(set(map(lambda x: int(''.join(x)), p(str(n))))))
    return -1 if l.index(n) == len(l)-1 else l[l.index(n)+1]
print(next_bigger(12345678210))