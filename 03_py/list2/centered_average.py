def centered_average(nums):
  small = nums[0]
  big = nums[0]
  
  for i in nums:
    small = min(small, i)
    big = max(big, i)
  
  list = nums
  list.remove(small)
  list.remove(big)
  
  total = 0
  
  for i in list:
    total += i
    
  return total / len(list)
