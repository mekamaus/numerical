def secant(f, p0 = 0, p1 = 1, tolerance = 0.01, n0 = 100):
  p0 = float(p0)
  p1 = float(p1)
  q0 = f(p0)
  q1 = f(p1)
  for i in range(2, n0 + 1):
    p = p1 - q1 * (p1 - p0) / (q1 - q0)
    print('{0}: {1}'.format(i, p))
    if abs(p - p1) < tolerance:
      return p
    p0, q0 = p1, q1
    p1, q1 = p, f(p)
  return None
