def array_front9(nums):
  
  for index in range(len(nums)):
    if (index == 3):
      break
    if nums[index] == 9:
      return True
      
  return False
