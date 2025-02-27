class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsi = dict()
        charsj = dict()
        for i in s:
            if i not in charsi:
                charsi[i] = 1
            else:
                charsi[i] += 1
        for j in t:
            if j not in charsj:
                charsj[j] = 1
            else:
                charsj[j] += 1
        
        return charsi == charsj
