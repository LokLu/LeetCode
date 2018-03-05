class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result =[]
        for i in range (0,rowIndex+1):
            result.insert(0,1)
            if i>1:
                for j in range (1,i):
                    result[j]+=result[j+1]
                    
        return result
