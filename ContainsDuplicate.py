class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set()

        for i in nums:
            if i not in check_set:
                check_set.add(i)
            else:
                return True
                
        return False
