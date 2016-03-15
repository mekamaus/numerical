def steffensen(g, p0 = 0, tolerance = 0.01, n0 = 100):
  for i in range(1, n0 + 1):
    p1 = g(p0)
    p2 = g(p1)
    print('  p1({0}) = {1}'.format(i - 1, p1))
    print('  p2({0}) = {1}'.format(i - 1, p2))
    p = p0 - (p1 - p0) ** 2 / (p2 - 2 * p1 + p0)
    print('p0({0}) = {1}'.format(i, p))
    if abs(p - p0) < tolerance:
      return p
    p0 = p
