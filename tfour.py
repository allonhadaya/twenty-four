from sys import argv
from itertools import product, permutations, repeat

def main():
# operands = [float(x) for x in argv[1:]]

  operators = [add, sub, mul, div]
  symbols = { add: '+', sub: '-', mul: '*', div: '/' }

# for s in solutions(operators, operands, 24):
#   print present(s, symbols)

  a = b = c = 0
  for operands in allOps():
    s = len(solutions(operators, operands, 24))
    b = b + 1
    if s > 0:
      a = a + 1
      c = c + s
    
  print '''
a = %d
b = %d
c = %d
a / b = %d / %d = %f
c / a = %d / %d = %f
c / b = %d / %d = %f
''' % (a, b, c, a, b, float(a) / b, c, a, float(c) / a, c, b, float(c) / b)

def solutions(operators, operands, target):
  numberOfOperators = len(operands) - 1
  options = [evaluate(a, b) for a in permutations(operands) for b in product(operators, repeat=numberOfOperators)]
  return [o for o in options if o[2] == target]

def evaluate(operands, operators):
  try:
    result = operands[0]
    for i in range(len(operators)):
      result = operators[i](result, operands[i+1])
  except:
    result = None
  return (operands, operators, result)

def present(solution, symbols):
  numOps = len(solution[1])
  value = '(' * numOps + str(solution[0][0])
  for i in range(numOps):
    value = value + ' ' + symbols[solution[1][i]] + ' ' + str(solution[0][i + 1]) + ')'
  return value

def allOps():
  for a in range(1, 14):
    for b in range(1, 14):
      for c in range(1, 14):
        for d in range(1, 14):
          yield [a, b, c, d]

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

main()
