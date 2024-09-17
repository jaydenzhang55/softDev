def sum13(nums):
  total = 0
  
  if len(nums) == 0:
    return 0
  else:
    for index in range(len(nums)):
      total += nums[index]
      if (nums[index] == 13) and (index + 1 != len(nums)) and (nums[index + 1] != 13):
        total -= nums[index]
        total -= nums[index + 1]
      elif nums[index] == 13:
        total -= nums[index]
        
        
  return total
