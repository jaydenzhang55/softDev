def max_end3(nums):
  larger = 0
  if nums[0] > nums[2]:
    larger = nums[0]
  else: 
    larger = nums[2]
  
  return [larger, larger, larger]
