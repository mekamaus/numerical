from cmath import sqrt

def muller(f, p0, p1, p2, tolerance = 0.01, n0 = 100):
  p0, p1, p2 = float(p0), float(p1), float(p2)
  h1 = p1 - p0
  h2 = p2 - p1
  d1 = (f(p1) - f(p0)) / h1
  d2 = (f(p2) - f(p1)) / h2
  d = (d2 - d1) / (h2 + h1)
  for i in range(3, n0):
    b = d2 + h2 * d
    D = sqrt(b**2 - 4*f(p2)*d)
    if abs(b - D) < abs(b + D):
      E = b + D
    else:
      E = b - D
    h = -2 * f(p2) / E
    p = p2 + h
    if abs(h) < tolerance:
      return p
    p0 = p1
    p1 = p2
    p2 = p
    h1 = p1 - p0
    h2 = p2 - p1
    d1 - (f(p1) - f(p0)) / h1
    d2 = (f(p2) - f(p1)) / h2
    d = (d2 - d1) / (h2 + h1)
