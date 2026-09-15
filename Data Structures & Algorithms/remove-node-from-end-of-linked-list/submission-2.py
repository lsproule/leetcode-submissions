# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast  = head.next 
        length = 2
        if head.next == None and n == 1:
            return None

        while fast and fast.next:
            length += 2
            fast = fast.next.next
        if fast:
            length += 1 

        steps = length - n - 1
        node = head

        if steps == 0:
            head = head.next
            return head
    
        while steps - 1 >= 2:
            node = node.next.next
            steps -= 2
        if steps - 1:
            node = node.next
        
        if node.next: 
            node.next = node.next.next
        return head

        
