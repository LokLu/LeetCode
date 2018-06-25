# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        slow = head
        fast = head
        for i in range (0, n):
            fast = fast.next
        
        if fast==None:
            head = head.next
            return head
        
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return head
