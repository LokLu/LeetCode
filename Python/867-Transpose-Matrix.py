class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(A),len(A[0])
        result = [[None]*r for _ in range(0,c)]
        
        for i in range (0, r):
            for j in range (0, c):
                result[j][i] = A[i][j]
        
        return result

    
# solution 2    
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[row[i] for row in A] for i in range(len(A[0]))]
