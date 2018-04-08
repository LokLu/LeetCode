class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        x = collections.Counter(nums)
        for i in x:
            if (k>0 and i+k in x) or (k==0 and x[i]>1):
                result+=1

        return result
