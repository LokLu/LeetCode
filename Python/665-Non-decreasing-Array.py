class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = nums[0]
        count = 0
        for i in range (1,len(nums)):
            if nums[i]<last:
                if i>1 and i<len(nums)-1:
                    if nums[i+1]>nums[i-1] or nums[i]>nums[i-2]:
                        count+=1
                    else:
                        return False
                else:
                    count+=1
            last = nums[i]  
            
        return False if count>1 else True
