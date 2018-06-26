# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
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

class Solution(object):

    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow  = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
        fast = head
        slow = reverseList(slow)
        
        while slow and fast:
            if slow.val!=fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True
        
        
        
        
