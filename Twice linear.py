a = [1]

def y_line(n):
    yl = [1]
    while len(yl) < n // 2:
        yl += [2 * yl[-1] + 1]
    return yl

def z_line(n):
    zl = [1]
    while len(zl) < n // 2:
        zl += [3 * zl[-1] + 1]
    return zl

def z_for_y(yl):
    zl2 = []
    for i in yl:
        zl2 += [3 * i + 1]
    return list(set(zl2 + yl))

def y_for_z(zl):
    yl2 = []
    for i in zl:
        yl2 += [3 * i + 1]
    return list(set(yl2 + zl))

def dbl_linear(n):
    return list(sorted(y_for_z(z_line(n)) + z_for_y(y_line(n))))

print(dbl_linear(10))


