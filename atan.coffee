threshold = 0.001

min = (-threshold + Math.PI) / 4
max = (threshold + Math.PI) / 4

i = 0
sum = 0
while sum < min or sum > max
  i++
  sum += Math.pow(-1, i + 1) / (2 * i - 1)
  console.log i, sum
