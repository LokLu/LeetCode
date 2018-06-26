# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        elif head.next==None:
            return head
        else:
        
            cur = head
            dummy_odd = odd_cur =  ListNode(0)
            dummy_even = even_cur = ListNode(0)

            index = 1
            
            while cur!=None:
 
                odd_cur.next = cur
                odd_cur = odd_cur.next
                even_cur.next = cur.next
                even_cur = even_cur.next
                cur = cur.next.next if even_cur else None
                
            odd_cur.next = dummy_even.next
        
            return dummy_odd.next
        
        
