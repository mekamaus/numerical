def bisect(f, a, b, tolerance=0.001, n0=10):
    i = 1
    fa = f(float(a))
    while i <= n0:
        p = float(a) + float(b - a) / 2
        fp = f(float(p))
        print(a, p, b)
        if fp == 0 or float(b - a) / 2 < tolerance:
            return p
        i += 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
    return None
