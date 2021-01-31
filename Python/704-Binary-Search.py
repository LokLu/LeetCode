class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums)-1
        
        while end-start>=0:
            middle = (start+end)/2
            if nums[middle]>target:
                end = middle-1
            elif nums[middle]<target:
                start = middle+1
            else:
                return middle
            
        return -1
