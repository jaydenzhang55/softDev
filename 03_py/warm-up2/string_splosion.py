def string_splosion(str):
  str1 = ''
  for index in range(len(str)):
    str1 += str[0:index + 1]
    
  return str1
