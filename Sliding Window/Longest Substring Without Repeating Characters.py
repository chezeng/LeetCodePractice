class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        char_index = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            
            else:
                max_length = max(max_length, r - l + 1)
        
            char_index[s[r]] = r
        
        return max_length
        
