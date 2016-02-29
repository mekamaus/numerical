def converge(f, p0=1):
  p = p0
  print('0: ' + str(p))
  for i in range(20):
    p = f(float(p))
    print(str(i + 1) + ': ' + str(p))
