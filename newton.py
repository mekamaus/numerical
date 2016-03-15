from sympy import *

def newton(fn, p0 = 0, tolerance = 0.01, n0 = 100):
  x = Symbol('x')
  f = lambda x0: fn(x).subs(x, x0).evalf()
  fd = lambda x0: diff(fn(x), x).subs(x, x0).evalf()

  g = lambda x: (x - f(x) / fd(x)).evalf()

  p0 = float(p0)

  for i in range(n0):
    p = p0 - (f(p0) / fd(p0)).evalf()
    print('{0}: {1}'.format(i + 1, p))
    if abs(p - p0) < tolerance:
      return p
    p0 = p
  return None

def newton_mod(fn, p0 = 0, tolerance = 0.01, n0 = 100):
  x = Symbol('x')
  f = lambda x0: fn(x).subs(x, x0).evalf()
  fd = lambda x0: diff(fn(x), x).subs(x, x0).evalf()
  fdd = lambda x0: diff(fn(x), x, 2).subs(x, x0).evalf()

  g = lambda x: (x - (f(x) * fd(x)) / (fd(x) ** 2 - f(x) * fdd(x))).evalf()

  p0 = float(p0)

  for i in range(n0):
    p = g(p0)
    print('{0}: {1}'.format(i + 1, p))
    if abs(p - p0) < tolerance:
      return p
    p0 = p
  return None
