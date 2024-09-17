def array123(nums):
  for index in range(len(nums) - 2):
    if (nums[index] == 1) and (nums[index + 1] == 2) and (nums[index + 2] == 3):
      return True
    
  return False
