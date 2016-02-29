def fixedpoint(g, p0=1, tolerance=0.01, n0=100):
    for i in range(1, n0 + 1):
        p = g(float(p0))
        if abs(p - p0) < tolerance:
            return p
        p0 = p
    return None
