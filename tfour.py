from sys import argv
from itertools import product, permutations

def main():
  for s in solutions():
    print present(s)

def solutions():  
  options = [calc(a, b) for a in permutations(operands) for b in product(operators, repeat=3)]
  return [opt for opt in options if opt[2] == 24.0]

def calc(a, b):
  try:
    return (a, b, b[2](b[1](b[0](a[0], a[1]), a[2]), a[3]))
  except ZeroDivisionError:
    return (a, b, float('NaN'))

def present(opt):  
  return '%f = (((%f %s %f) %s %f) %s %f)' % (opt[2], opt[0][0], sym[opt[1][0]], opt[0][1], sym[opt[1][1]], opt[0][2], sym[opt[1][2]], opt[0][3])

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

operands = [float(x) for x in argv[1:5]]
operators = [add, sub, mul, div]
sym = { add: '+', sub: '-', mul: '*', div: '/' }

main()
