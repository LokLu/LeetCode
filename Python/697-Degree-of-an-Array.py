class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = []
        index_location=[]
        length = []
        count = []
        result = []
        for i in range (0,len(nums)):
            if nums[i] not in element:
                element.append(nums[i])
                index_location.append([i,i])
                length.append(1)
                count.append(1)
            else:
                index = element.index(nums[i])
                index_location[index][1]=i
                length[index] = index_location[index][1]-index_location[index][0]+1
                count[index] +=1
        
        max_app = max(count)
        
        while count.count(max_app)>0:
            result.append(length.pop(count.index(max_app)))
            count.pop(count.index(max_app))
            
        return min(result)
        
