# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur!=None:
            if cur.next==None:
                break
            else:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = head
                head = tmp
        return head
            
