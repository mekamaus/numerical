
start = parseInt process.argv[2]
end = parseInt process.argv[3]

round = (num, digits) ->
  [before, after] = num.toString().split '.'
  digitsBeforeDecimal = if before is '0' or before is '-0' then 0 else if before[0] is '-' then before.length - 1 else before.length
  digits -= digitsBeforeDecimal
  after ?= '0'
  parseFloat before + '.' + after[0..(digits - 1)]

sum = 0.0
digits = 3
for i in [start..end]
  term = round 1 / (round (i * i), digits), digits
  sum = round sum + term, digits
  console.log i, sum

console.log sum

sum = 0.0
for i in [start..end]
 term = 1/ (i * i)
 sum += term

console.log sum
