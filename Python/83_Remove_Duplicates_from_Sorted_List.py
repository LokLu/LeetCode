# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur !=None:
            net = cur.next
            if net==None:
                break
            else:
                if net.val==cur.val:
                    cur.next = net.next
                else:
                    cur = cur.next

        return head
