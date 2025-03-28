class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        length = len(nums)

        for start in range(length - 2):
            if start > 0 and nums[start - 1] == nums[start]:
                continue
            
            target = -nums[start]
            left = start + 1
            right = length - 1

            while left < right:
                currentSum = nums[left] + nums[right]

                if target == currentSum:
                    result.append([nums[start], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif currentSum < target:
                    left += 1
                
                else:
                    right -= 1
        
        return result
