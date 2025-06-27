# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        else:


            length = 1
            current = head
            first = head
            while current.next:
                prev = current
                current = current.next
                length += 1
            current.next = first
            new_k = k % length
            node_break = length - new_k - 1 
        
            new_tail = first

            for _ in range(node_break):
                new_tail = new_tail.next

            new_head = new_tail.next
        
            new_tail.next = None

        return new_head
     
        

        
        



        



        