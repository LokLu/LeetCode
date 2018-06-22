class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
        result = []
        start = end = 0
        last = S[0]
        for i in range (1,len(S)):
            if S[i] == last:
                end+=1
            else:
                if end-start >=2 :
                    result.append([start,end])
                start = end = i
                last = S[i]
                
        if end-start >=2 :
            result.append([start,end])
                
        return result
