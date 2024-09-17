def string_bits(str):
  str1 = ''
  for index in range(len(str)):
    if (index % 2 == 0):
      str1 += str[index]
  
  return str1
    
