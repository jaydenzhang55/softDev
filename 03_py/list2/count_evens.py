def count_evens(nums):
  total = 0
  for i in nums:
    if i % 2 == 0:
      total += 1
  return total
