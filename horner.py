def horner(a, x0):
  n = len(a) - 1
  y = a[n]
  z = a[n]
  for j in reversed(range(1, n)):
    y = x0 * y + a[j]
    z = x0 * z + y
    print('  b{0} = {1} for P'.format(j, y))
    print('  b{0} = {1} for Q'.format(j - 1, z))
  y = x0 * y + a[0]
  print('b0 = {0} for P'.format(y))
  return y, z
