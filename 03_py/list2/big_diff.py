def big_diff(nums):
  small = nums[0]
  big = nums[0]
  for i in nums:
    small = min(small, i)
    big = max(big, i)
  
  return big - small
