class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from fractions import gcd
        import collections
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals)>=2
