class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = []
       
        for i in range (0,len(nums)):
            if len(m)<3 and (nums[i] not in m):
                m.insert(0,nums[i])
                m.sort()
            elif nums[i]>m[0] and (nums[i] not in m):
                m.pop(0)
                m.insert(0,nums[i])
                m.sort()
                
        if len(m)<3:
            return m[-1]
        else:
            return m[0]
