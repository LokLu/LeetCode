class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.samelowertree(p,q)

    def samelowertree(self,x,y):
        if x == y == None:
            return True
        elif x==None or y==None:
            return False
        elif x.val!=y.val:
            return False
        else:
            return self.samelowertree(x.left,y.left) and self.samelowertree(x.right,y.right)
