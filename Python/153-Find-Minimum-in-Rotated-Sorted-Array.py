class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start,end = 0,len(nums)-1
        mini = nums[-1]
        while end>=start:
            middle = (start+end)/2
            if nums[middle]<mini:
                end = middle
                mini = nums[middle]
            elif nums[middle]>mini:
                start = middle+1
            else:
                return nums[middle]
