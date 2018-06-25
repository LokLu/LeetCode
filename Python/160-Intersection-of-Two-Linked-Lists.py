# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        if curA == None or curB ==None:
            return None
        
        while curA != curB:
            if curA == None:
                curA = headB
            else:
                curA = curA.next
            if curB == None:
                curB = headA
            else:
                curB = curB.next
                
        return curA

        

        
