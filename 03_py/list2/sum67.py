def sum67(nums):
  total = 0
  isThereASix = False
  for index in range(len(nums)):
    if nums[index] == 6:
      isThereASix = True
    if isThereASix:
      if nums[index] != 7:
        continue
      else:
        isThereASix = False
    else:
      total += nums[index]
      
  return total
