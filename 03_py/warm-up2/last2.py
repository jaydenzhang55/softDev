def last2(str):
  if (len(str) <= 1):
    return 0
  
  total = 0
  for index in range(len(str) - 1):
    newStr = str[index] + str[index + 1]
    if (str[-2:]) == newStr:
      total += 1
  
  return total - 1
