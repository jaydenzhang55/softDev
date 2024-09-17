def has22(nums):
  for index in range(len(nums) - 1):
    if (nums[index] == 2) and (nums[index + 1] == 2):
      return True
      
  return False
