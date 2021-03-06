# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 and l2:
            add = l1.val+l2.val+carry
            sum = add%10
            carry = add/10
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            
        if l1==None:
            while l2:
                add = l2.val+carry
                sum = add%10
                carry = add/10
                cur.next = ListNode(sum)
                cur = cur.next
                l2 = l2.next
        elif l2==None:
            while l1:
                add = l1.val+carry
                sum = add%10
                carry = add/10
                cur.next = ListNode(sum)
                cur = cur.next
                l1 = l1.next
        
        if carry==1:
            cur.next = ListNode(1)
            
        return head.next
            
            
            
            
