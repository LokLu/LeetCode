# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        end = n
        
        while end-start>=0:
            middle = (start+end)/2
            if guess(middle)==1:
                start = middle+1
            elif guess(middle)==-1:
                end = middle-1
            else:
                return middle
            
        return 0
