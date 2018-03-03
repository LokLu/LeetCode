class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        repeat = nums[0]
        count = 1
        for i in range (1,len(nums)):
            if nums[i]==repeat:
                count +=1
            else:
                repeat = nums[i]
                count =1
            if count>len(nums)/2:
                break
        return repeat
