class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range (len(nums)):
            difference = target - nums[i]
            if nums[i] not in check:
                check[difference] = i
            else: 
                return [check[nums[i]], i]
        
        return [0, 0]
