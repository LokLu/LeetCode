class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []
        
        for i in range (0,numRows):
            rows=[1]*(i+1)
            if i>1:
                for j in range (1,i):
                    rows[j]=result[i-1][j-1]+result[i-1][j]
            result.insert(len(result),rows)
            
        return result
