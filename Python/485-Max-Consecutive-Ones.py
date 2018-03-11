class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxlength = 0
        start = 0
        end = 0
        nums.insert(0,0)
        nums.insert(len(nums),0)
        
        for i in range (1,len(nums)):
            if nums[i]==1 and nums[i-1]==0:
                start = i
                end = i
            elif nums[i]==1 and nums[i-1]==1:
                end+=1
            elif nums[i]==0 and nums[i-1]==1:
                length = end -start+1
                maxlength = max(length,maxlength) 
                
        return maxlength
