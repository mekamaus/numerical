import math

def newton(f, fd, p0 = 0, tolerance = 0.01, n0 = 100):
  p0 = float(p0)
  for i in range(n0):
    p = p0 - f(p0) / fd(p0)
    print('{0}: {1}'.format(i + 1, p))
    if abs(p - p0) < tolerance:
      return p
    p0 = p
  return None

def newton_mod(f, fd, fdd, p0 = 0, tolerance = 0.01, n0 = 100):
  p = float(p0)
  g = lambda x: (f(x) * fd(x)) / (fd(x) ** 2 - f(x) * fdd(x))
  for i in range(n0):
    p = g(p)
