# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        slow = fast = head
        n = 1
        
        while fast.next:
            n= n+1
            fast=fast.next

        fast = head
        
        for i in range (0,k%n):            
            fast = fast.next if fast.next else head
                
        while fast.next:
            slow,fast = slow.next,fast.next
        
        fast.next = head
        head = slow.next
        slow.next = None
        
        return head
            
