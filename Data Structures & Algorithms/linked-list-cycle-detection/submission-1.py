# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = None
        idx = 0
        if turtle is None:
            return False

        while turtle.next is not None:
            if hare is None:
                if turtle.next is None:
                    return False
                if turtle.next.next is None:
                    return False
                hare = turtle.next
                
            if turtle == hare or turtle == hare.next:
                return True

            if hare.next:
                if hare.next.next:
                    hare = hare.next.next
                else:
                    return False
            turtle = turtle.next
            idx += 1
        return False
            

    