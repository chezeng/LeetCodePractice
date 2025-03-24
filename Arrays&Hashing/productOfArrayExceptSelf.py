class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        result = []
        zeroNum = 0

        for i in nums:
            if i != 0:
                product *= i
            else:
                zeroNum += 1
        
        for j in nums:
            if j != 0 and zeroNum == 0:
                result.append(product // j)
            elif j == 0 and zeroNum <= 1:
                result.append(product)
            else:
                result.append(0)

        return result
        
