# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head
         
        while True:
            # if slow == None  or fast == None:
            #     return None
            # elif fast.next ==None:
            #     return None
            # else:
            #     slow = slow.next
            #     fast = fast.next.next
            #     if slow ==fast:
            #         break
                    
            if slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow ==fast:
                    break
            else:
                return None
                    
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
            
        return slow
