list = []
tuple = ()
dic = {}

def add(*args) :
  sum = 0
  for ele in args :
    sum += ele
  return sum

def multi(*args) :
  result = 1
  for ele in args :
    result *= ele
  return result