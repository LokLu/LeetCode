# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        d_head = ListNode(1)
        d_head.next = head
        pre = d_head
        
        while pre!=None:
            if pre.next==None:
                break
            elif pre.next.val==val:
                pre.next = pre.next.next
            else:
                pre = pre.next

        return d_head.next
                
