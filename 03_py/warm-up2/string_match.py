def string_match(a, b):
  total = 0
  smaller = ''
  if (len(a) > len(b)):
    smaller = b
  else:
    smaller = a
  
  if (smaller < 2):
    if a == b:
      return 1
    else:
      return 0
  
  for index in range(len(smaller) - 1):
    if (a[index] + a[index+1]) == (b[index] + b[index + 1]):
      total += 1
  
  return total
