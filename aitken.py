def aitken(p0, pf, n0):
  print('Original Sequence')
  p = p0

  if type(pf) == type([]):
    sequence = pf
  elif type(pf) == type(lambda x: x):
    sequence = [0] * (n0 + 3)
    for i in range(n0 + 3):
      sequence[i] = p
      if i <= n0:
        print('{0}: {1}'.format(i, p))
      p = pf(p)

  print('')
  print('Aitken Sequence')

  for i in range(1, n0 + 1):
    ph = sequence[i] - (sequence[i + 1] - sequence[i]) ** 2 / (sequence[i + 2] - 2 * sequence[i + 1] + sequence[i])
    print('{0}: {1}'.format(i, ph))
