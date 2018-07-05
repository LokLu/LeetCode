class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start,end = 0,len(nums)-1
        
        while end>=start:
            middle = (start+end)/2

            if nums[middle]< (nums[middle-1] if middle-1>=0 else float('-Inf')):
                end = middle
            elif nums[middle]< (nums[middle+1] if middle+1<len(nums) else float('-Inf')):
                start = middle+1
            else:
                return middle
            
        return middle
                
