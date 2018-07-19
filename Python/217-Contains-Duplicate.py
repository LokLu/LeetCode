#1
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return False
        else:
            nums.sort()
            s = nums[0]
            for i in range (1,len(nums)):
                if nums[i]==s:
                    return True
                else:
                    s = nums[i]
        return False

#2
class Solution(object):
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    return True if len(nums)-len(set(nums))>0 else False
