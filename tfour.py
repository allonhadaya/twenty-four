from sys import argv
from itertools import product, permutations, combinations, repeat

def main():
  operands = [float(x) for x in argv[1:]]
  operators = [add, sub, mul, div]
  symbols = { add: '+', sub: '-', mul: '*', div: '/' }

  for s in solutions(operators, operands, 24):
    print present(s, symbols)

  deckOfCards = range(1, 14) + range(1, 14) + range(1, 14) + range(1, 14)
  allOperands = combinations(deckOfCards, 4)

#  numerator = devisor = 0
#  for operands in allOperands:
#    devisor = devisor + 1
#    if len(solutions(operators, operands, 24)) > 0:
#      numerator = numerator + 1

#  print 'all:%d' % devisor
#  print 'solutions:%d' % numerator
#  print 'probability of having a solution:%f' % (float(numerator) / devisor)

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

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

main()
