class Solution(object):
    def topKFrequent(self, nums, k):
        kv = dict()
        vk = dict()
        result = list()

        for i in nums:
            if i not in kv:
                kv[i] = 1
            else:
                kv[i] += 1
            
        for key, val in kv.items():
            if val not in vk:
                vk[val] = [key]
            else:
                vk[val].append(key)

        while (k > 0):
            m = max(vk.keys())
            l = vk[m]
            result.append(l[0])
            if (len(l) == 1):
                vk.pop(m)
            else:
                l.pop(0)
            k -= 1
        
        return result
        
