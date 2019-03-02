class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        split = s.split(' ')
        return len(split) - split.count('')
