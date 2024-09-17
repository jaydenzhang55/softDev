def front_back(str):
  if (len(str) == 0):
    return ''
  newStr = str
  newStr = newStr.replace(str[0], str[-1], 1)
  newNewStr = newStr[0:-1]
  
  return newNewStr + str[0]
