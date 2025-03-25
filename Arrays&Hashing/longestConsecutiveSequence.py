class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        nums.sort()

        oldLength = 1
        newLength = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue

            if nums[i + 1] == nums[i] + 1:
                newLength += 1

            else:
                if oldLength < newLength:
                    oldLength = newLength
                newLength = 1

        return max(oldLength, newLength)
        
