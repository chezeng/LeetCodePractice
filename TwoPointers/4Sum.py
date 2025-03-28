class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        nums.sort()
        length = len(nums)

        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                goal = target - (nums[i] + nums[j])
                left = j + 1
                right = length - 1

                while left < right:
                    currentSum = nums[left] + nums[right]
                    if currentSum == goal:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif currentSum < goal:
                        left += 1
                    
                    else:
                        right -= 1
            
        return result

                
                
