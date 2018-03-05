class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)==1:
            return True
            
        for i in range (1,len(matrix)):
            if matrix[i][1:]!=matrix[i-1][0:-1]:
                return False
        return True
