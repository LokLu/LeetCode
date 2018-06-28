class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []
        
        while matrix:
            if matrix[0]!=0:
                result.extend(matrix.pop(0))

                if matrix :
                    i=0
                    for _ in range (0,len(matrix)-1):
                        result.append(matrix[i].pop(-1))
                        i+=1
                        if len(matrix[0])==0:
                            matrix.pop(0)
                            i-=1

                if matrix :
                    new = matrix.pop(-1)
                    new.reverse()
                    result.extend(new)

                if matrix :
                    i=len(matrix)-1
                    for _ in range (0,len(matrix)):
                        result.append(matrix[i].pop(0))
                        i-=1
                        if len(matrix[-1])==0:
                            matrix.pop(-1)
                    print result
            
        return result
        
