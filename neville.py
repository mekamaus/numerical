def neville(f, x, xs):
  n = len(xs) - 1
  q = [([f(xi)] + [0] * n) for xi in xs]
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      q[i][j] = ((x - xs[i - j]) * q[i][j - 1] - (x - xs[i]) * q[i - 1][j - 1]) / (xs[i] - xs[i - j])
  return q[n][n]
